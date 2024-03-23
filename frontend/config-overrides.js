const postCSSConfig = require('./postcss.config');

module.exports = function override(config, env) {
  // Find the rule for CSS files
  const cssRule = config.module.rules.find(rule => rule.oneOf && rule.oneOf.find(r => r.test && r.test.toString() === '/\\.css$/'));

  // Add PostCSS loader
  cssRule.oneOf.unshift({
    test: /\.css$/,
    use: [
      'style-loader',
      'css-loader',
      {
        loader: 'postcss-loader',
        options: {
          postcssOptions: postCSSConfig,
        },
      },
    ],
  });

  return config;
};
