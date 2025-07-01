/* Giscus Comments Integration for MkDocs Material */

document.addEventListener('DOMContentLoaded', function() {
  // Check if comments are enabled and we have the necessary configuration
  const commentsEnabled = document.querySelector('[data-md-component="comments"]');
  
  if (commentsEnabled) {
    // Get the current theme (light/dark)
    const getGiscusTheme = () => {
      const palette = document.querySelector('[data-md-color-scheme]');
      if (palette) {
        const scheme = palette.getAttribute('data-md-color-scheme');
        return scheme === 'slate' ? 'dark' : 'light';
      }
      return 'light';
    };

    // Initialize Giscus
    const initGiscus = () => {
      const script = document.createElement('script');
      script.src = 'https://giscus.app/client.js';
      script.setAttribute('data-repo', 'yourusername/your-repo'); // Replace with actual repo
      script.setAttribute('data-repo-id', process.env.GISCUS_REPO_ID || ''); // Set via environment
      script.setAttribute('data-category', 'General');
      script.setAttribute('data-category-id', process.env.GISCUS_CATEGORY_ID || ''); // Set via environment
      script.setAttribute('data-mapping', 'pathname');
      script.setAttribute('data-strict', '0');
      script.setAttribute('data-reactions-enabled', '1');
      script.setAttribute('data-emit-metadata', '1');
      script.setAttribute('data-input-position', 'bottom');
      script.setAttribute('data-theme', getGiscusTheme());
      script.setAttribute('data-lang', 'en');
      script.setAttribute('data-loading', 'lazy');
      script.crossOrigin = 'anonymous';
      script.async = true;

      // Find the comments container and append the script
      const commentsContainer = document.querySelector('[data-md-component="comments"]');
      if (commentsContainer) {
        commentsContainer.appendChild(script);
      }
    };

    // Update Giscus theme when Material theme changes
    const updateGiscusTheme = () => {
      const giscusFrame = document.querySelector('iframe.giscus-frame');
      if (giscusFrame) {
        const theme = getGiscusTheme();
        giscusFrame.contentWindow.postMessage(
          { giscus: { setConfig: { theme } } },
          'https://giscus.app'
        );
      }
    };

    // Listen for theme changes
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'attributes' && mutation.attributeName === 'data-md-color-scheme') {
          setTimeout(updateGiscusTheme, 100); // Small delay to ensure theme has changed
        }
      });
    });

    // Start observing theme changes
    const paletteElement = document.querySelector('[data-md-color-scheme]');
    if (paletteElement) {
      observer.observe(paletteElement, { attributes: true });
    }

    // Initialize Giscus when the page loads
    initGiscus();
  }
});