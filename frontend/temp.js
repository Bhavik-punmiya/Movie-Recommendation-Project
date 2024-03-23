import React from 'react';
import './card.css'; // Ensure this path is correct

function MovieCard({ title, overview, poster_path, homepage }) {
    return (
        <div className="content-wrapper">
            <div className="content-wrapper">
                {/* Repeat the following block for each news card */}
                <div className="news-card">
                    <a href={homepage} className="news-card__card-link"></a>
                    <img src={`https://image.tmdb.org/t/p/w500${poster_path}&h=750&w=1260`} alt={title} className="news-card__image" />
                    <div className="news-card__text-wrapper">
                        <h2 className="news-card__title">{title}</h2>
                        <div className="news-card__post-date">Jan 29, 2018</div>
                        <div className="news-card__details-wrapper">
                            <p className="news-card__excerpt">{overview}</p>
                            <a href={homepage} className="news-card__read-more">Read more <i className="fas fa-long-arrow-alt-right"></i></a>
                        </div>
                    </div>
                </div>
                {/* Repeat the block above for each news card */}
            </div>
        </div>
    );
}

export default MovieCard;
