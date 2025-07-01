/* Enhanced Search Functionality for MkDocs Material */

document.addEventListener('DOMContentLoaded', function() {
  
  // Enhanced search with keyboard shortcuts
  const setupSearchShortcuts = () => {
    document.addEventListener('keydown', function(e) {
      // Focus search with '/' key
      if (e.key === '/' && !e.ctrlKey && !e.metaKey && !e.altKey) {
        const searchInput = document.querySelector('.md-search__input');
        const activeElement = document.activeElement;
        
        // Don't trigger if already in an input field
        if (activeElement && (
          activeElement.tagName === 'INPUT' || 
          activeElement.tagName === 'TEXTAREA' || 
          activeElement.contentEditable === 'true'
        )) {
          return;
        }
        
        e.preventDefault();
        if (searchInput) {
          searchInput.focus();
        }
      }
      
      // Escape to close search
      if (e.key === 'Escape') {
        const searchInput = document.querySelector('.md-search__input');
        if (searchInput && document.activeElement === searchInput) {
          searchInput.blur();
          searchInput.value = '';
        }
      }
    });
  };
  
  // Search analytics and tracking
  const setupSearchAnalytics = () => {
    const searchInput = document.querySelector('.md-search__input');
    if (!searchInput) return;
    
    let searchTimeout;
    
    searchInput.addEventListener('input', function(e) {
      clearTimeout(searchTimeout);
      
      // Debounce search tracking
      searchTimeout = setTimeout(() => {
        const query = e.target.value.trim();
        if (query.length > 2) {
          // Track search queries (if analytics is enabled)
          if (typeof gtag !== 'undefined') {
            gtag('event', 'search', {
              search_term: query
            });
          }
          
          // Log search for debugging (remove in production)
          console.log('Search query:', query);
        }
      }, 1000);
    });
  };
  
  // Enhanced search results with highlighting
  const enhanceSearchResults = () => {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList') {
          const searchResults = document.querySelectorAll('.md-search-result__item');
          
          searchResults.forEach((result, index) => {
            // Add result numbering
            if (!result.querySelector('.search-result-number')) {
              const numberSpan = document.createElement('span');
              numberSpan.className = 'search-result-number';
              numberSpan.textContent = `${index + 1}`;
              numberSpan.style.cssText = `
                display: inline-block;
                width: 20px;
                height: 20px;
                background: var(--md-accent-fg-color);
                color: white;
                border-radius: 50%;
                text-align: center;
                font-size: 0.7rem;
                line-height: 20px;
                margin-right: 0.5rem;
                font-weight: bold;
              `;
              
              const title = result.querySelector('.md-search-result__title');
              if (title) {
                title.insertBefore(numberSpan, title.firstChild);
              }
            }
            
            // Add keyboard navigation
            result.addEventListener('keydown', function(e) {
              if (e.key === 'Enter') {
                const link = this.querySelector('a');
                if (link) {
                  link.click();
                }
              }
            });
          });
        }
      });
    });
    
    const searchResults = document.querySelector('.md-search-result');
    if (searchResults) {
      observer.observe(searchResults, { childList: true, subtree: true });
    }
  };
  
  // Search suggestions and autocomplete
  const setupSearchSuggestions = () => {
    const searchInput = document.querySelector('.md-search__input');
    if (!searchInput) return;
    
    // Common search terms and suggestions
    const suggestions = [
      'getting started',
      'installation',
      'configuration',
      'customization',
      'features',
      'blog',
      'comments',
      'versioning',
      'deployment',
      'troubleshooting'
    ];
    
    searchInput.addEventListener('focus', function() {
      // Could implement autocomplete dropdown here
      this.setAttribute('placeholder', 'Search documentation... (Press / to focus)');
    });
    
    searchInput.addEventListener('blur', function() {
      this.setAttribute('placeholder', 'Search');
    });
  };
  
  // Search result click tracking
  const setupSearchTracking = () => {
    document.addEventListener('click', function(e) {
      const searchResult = e.target.closest('.md-search-result__item');
      if (searchResult) {
        const title = searchResult.querySelector('.md-search-result__title')?.textContent;
        const url = searchResult.querySelector('a')?.href;
        
        // Track search result clicks
        if (typeof gtag !== 'undefined' && title) {
          gtag('event', 'select_content', {
            content_type: 'search_result',
            item_id: url,
            item_name: title
          });
        }
        
        console.log('Search result clicked:', { title, url });
      }
    });
  };
  
  // Initialize all search enhancements
  setupSearchShortcuts();
  setupSearchAnalytics();
  enhanceSearchResults();
  setupSearchSuggestions();
  setupSearchTracking();
  
  // Add search help tooltip
  const addSearchHelp = () => {
    const searchForm = document.querySelector('.md-search');
    if (!searchForm) return;
    
    const helpButton = document.createElement('button');
    helpButton.innerHTML = '?';
    helpButton.className = 'md-search__help';
    helpButton.title = 'Search Help: Use / to focus, Escape to close, Enter to search';
    helpButton.style.cssText = `
      position: absolute;
      right: 10px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: 1px solid var(--md-default-fg-color--lighter);
      border-radius: 50%;
      width: 20px;
      height: 20px;
      font-size: 0.7rem;
      color: var(--md-default-fg-color--light);
      cursor: help;
      z-index: 1;
    `;
    
    helpButton.addEventListener('click', function(e) {
      e.preventDefault();
      alert(`Search Help:
      
• Press "/" to focus search
• Press "Escape" to close search  
• Use quotes for exact phrases: "getting started"
• Use - to exclude terms: features -blog
• Search is case-insensitive
• Partial matches are supported`);
    });
    
    const searchInner = searchForm.querySelector('.md-search__inner');
    if (searchInner) {
      searchInner.style.position = 'relative';
      searchInner.appendChild(helpButton);
    }
  };
  
  // Add search help after a short delay to ensure DOM is ready
  setTimeout(addSearchHelp, 500);
  
});

// Export for potential external use
window.MkDocsSearchEnhancements = {
  version: '1.0.0',
  initialized: true
};