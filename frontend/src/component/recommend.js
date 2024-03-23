import React, { useState, useEffect } from 'react';
import axios from 'axios'; // Import axios
import Box from '@mui/material/Box';
import InputBase from '@mui/material/InputBase';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import Paper from '@mui/material/Paper';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import MovieCard from '../component/card';
const apiKey = 'Your TDMBAPI KEY ';
const baseUrl = 'https://api.themoviedb.org/3';
const searchEndpoint = '/search/movie';

export default function Recommend() {
 const [searchTerm, setSearchTerm] = useState('');
 const [movieDetails, setMovieDetails] = useState([]); // State to hold movie details

 const handleSearch = async (event) => {
      if (event.key === 'Enter' || event.type === 'click') {
         event.preventDefault(); // Only prevent default for Enter key or click event
         const apiUrl = 'http://127.0.0.1:5000/recommend_post';
         const data = { movie: searchTerm };
     
         try {
           const response = await axios.post(apiUrl, data); // Use axios.post for making the request
           const json = JSON.parse(response.data)
           const movieobjects = await cleanMovieTitles(json)
           const moviesid = await searchAllMoviesAndGetIds(movieobjects)
           const details = await fetchAllMovieDetails(moviesid)
           console.log(details)
           setMovieDetails(details); // Update movieDetails state with fetched details
         } catch (error) {
           console.error('Error fetching data:', error);
         }
      }
 };
// Function to search for a movie by title and retrieve its ID
async function searchMovieAndGetId(title) {
    const query = encodeURIComponent(title);
    const url = `${baseUrl}${searchEndpoint}?api_key=${apiKey}&query=${query}`;

    try {
        const response = await axios.get(url);
        if (response.status === 200 && response.data.results.length > 0) {
            return response.data.results[0].id; // Assuming the first result is the one you're interested in
        } else {
            console.error(`No results found for "${title}"`);
            return null;
        }
    } catch (error) {
        console.error(`Error fetching data for "${title}":`, error);
        return null;
    }
}

function cleanMovieTitles(movies) {
  movies.forEach(movie => {
      movie.clean_title = movie.title.replace(/\s*\([^)]*\)/, '');
  });
  return movies;
}
 
 
async function searchAllMoviesAndGetIds(movies) {
  const movieIdPromises = movies.map(movie => searchMovieAndGetId(movie.clean_title));
  const movieIds = await Promise.all(movieIdPromises);
  
  const movieIdMap = {};
  movieIds.forEach((movieId, index) => {
      movieIdMap[movies[index].clean_title] = movieId;
  });

  for (const title in movieIdMap) {
      console.log(`${title}: ${movieIdMap[title]}`);
  }

  return movieIdMap;
}

async function fetchMovieDetails(movieId) {
  try {
      const response = await axios.get(`https://api.themoviedb.org/3/movie/${movieId}?api_key=87fd974feb9f46fbd46d0db9f4e7930c`);
      return response.data;
  } catch (error) {
      // If an error occurs or no data found, return null
      console.error(`Error fetching details for movie ID ${movieId}:`, error);
      return null;
  }
}

async function fetchAllMovieDetails(movieIdMap) {
  const movieDetailsPromises = Object.entries(movieIdMap).map(([title, id]) => {
       return fetchMovieDetails(id)
           .then(movieDetails => ({ title, details: movieDetails }))
           .catch(error => {
               console.error(`Error fetching details for ${title}:`, error);
               return { title, details: null };
           });
  });
 
  const movieDetails = await Promise.all(movieDetailsPromises);
  return movieDetails.filter(movie => movie.details !== null); // Filter out movies without details
 }

return (
  <Box
     sx={{
       display: 'flex',
       flexDirection: 'column',
       alignItems: 'center',
       minHeight: '100vh',
       padding: '20px',
     }}
  >
     <Paper
       component="form"
       sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: 800,     backgroundColor: 'hsl(0deg 0% 18.04%)', // Set the background color
       '& .MuiInputBase-input': {
         color: 'white', // Set the text color
       }, }}
     >
       <InputBase
       
       sx={{
        ml: 1,
        flex: 1,
        backgroundColor: 'hsl(0deg 0% 18.04%)', // Set the background color
        '& .MuiInputBase-input': {
          color: 'white', // Set the text color
        },
     }}

         placeholder="Search for Similar Movies"
         inputProps={{ 'aria-label': 'search google maps' }}
         value={searchTerm}
         onChange={(e) => {setSearchTerm(e.target.value)}}
         onKeyPress={handleSearch}
       />
       <IconButton type="button" sx={{ p: '10px' }} aria-label="search" onClick={handleSearch}>
         <SearchIcon sx={{ color: 'white' }}  />
       </IconButton>
     </Paper>
     <Box sx={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: 2 , padding: '0 10rem'}}>
       {movieDetails.map((movie, index) => (
         <MovieCard key={index} title={movie.title} overview={movie.details.overview} poster_path={movie.details.poster_path} homepage={movie.details.homepage} />
       ))}
     </Box>
  </Box>
 );
}