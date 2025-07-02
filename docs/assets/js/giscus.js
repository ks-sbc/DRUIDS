/* Giscus Comments Integration for MkDocs Material */

// This file handles the client-side Giscus integration
// The actual Giscus script is loaded in comments.html partial

document.addEventListener('DOMContentLoaded', function() {
  // Function to update Giscus theme when Material theme changes
  const updateGiscusTheme = () => {
    const iframe = document.querySelector('iframe.giscus-frame');
    if (!iframe) return;
    
    // Get current Material theme
    const palette = __md_get("__palette");
    if (palette && typeof palette.color === "object") {
      const theme = palette.color.scheme === "slate" ? "dark" : "light";
      
      // Send message to Giscus iframe to update theme
      iframe.contentWindow.postMessage(
        { giscus: { setConfig: { theme } } },
        'https://giscus.app'
      );
    }
  };
  
  // Listen for Material theme changes
  const ref = document.querySelector("[data-md-component=palette]");
  if (ref) {
    ref.addEventListener("change", function() {
      // Small delay to ensure theme has fully changed
      setTimeout(updateGiscusTheme, 100);
    });
  }
  
  // Initial theme sync (handled by comments.html, but this is a backup)
  setTimeout(updateGiscusTheme, 1000);
});