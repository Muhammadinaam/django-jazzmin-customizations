/**
 * Sidebar Search for Django Admin with Jazzmin
 * Adds a search box to filter menu items
 */
document.addEventListener('DOMContentLoaded', function() {
    // Find the sidebar navigation
    const sidebar = document.querySelector('.main-sidebar');
    if (!sidebar) return;
    
    const navMenu = sidebar.querySelector('nav');
    if (!navMenu) return;
    
    // Create search wrapper
    const searchWrapper = document.createElement('div');
    searchWrapper.className = 'sidebar-search-wrapper';
    searchWrapper.innerHTML = `
        <input type="text" 
               class="sidebar-search" 
               placeholder="🔍 Search menu (Ctrl+K)..." 
               aria-label="Search menu items">
    `;
    
    // Insert search box at the top of navigation
    navMenu.insertBefore(searchWrapper, navMenu.firstChild);
    
    // Create no results message
    const noResultsMsg = document.createElement('div');
    noResultsMsg.className = 'no-results-message';
    noResultsMsg.textContent = 'No menu items found';
    navMenu.appendChild(noResultsMsg);
    
    const searchInput = searchWrapper.querySelector('.sidebar-search');
    
    // Get all menu items
    const menuGroups = navMenu.querySelectorAll('.nav-item.has-treeview, .nav-item');
    
    // Search function
    function performSearch(query) {
        query = query.toLowerCase().trim();
        let visibleCount = 0;
        
        if (query === '') {
            // Show all items
            menuGroups.forEach(group => {
                group.classList.remove('menu-item-hidden');
                // Remove highlights
                const links = group.querySelectorAll('.nav-link');
                links.forEach(link => {
                    removeHighlights(link);
                });
            });
            noResultsMsg.classList.remove('show');
            return;
        }
        
        // Search through menu items
        menuGroups.forEach(group => {
            const links = group.querySelectorAll('.nav-link');
            let groupHasMatch = false;
            
            links.forEach(link => {
                const text = link.textContent.toLowerCase();
                
                if (text.includes(query)) {
                    groupHasMatch = true;
                    highlightText(link, query);
                }
            });
            
            if (groupHasMatch) {
                group.classList.remove('menu-item-hidden');
                // Expand the group if it's collapsible
                if (group.classList.contains('has-treeview')) {
                    group.classList.add('menu-open');
                }
                visibleCount++;
            } else {
                group.classList.add('menu-item-hidden');
            }
        });
        
        // Show/hide no results message
        if (visibleCount === 0) {
            noResultsMsg.classList.add('show');
        } else {
            noResultsMsg.classList.remove('show');
        }
    }
    
    // Remove highlights
    function removeHighlights(element) {
        const highlights = element.querySelectorAll('.search-highlight');
        highlights.forEach(highlight => {
            const text = highlight.textContent;
            highlight.replaceWith(document.createTextNode(text));
        });
    }
    
    // Highlight matching text
    function highlightText(element, query) {
        removeHighlights(element);
        
        const walker = document.createTreeWalker(
            element,
            NodeFilter.SHOW_TEXT,
            null,
            false
        );
        
        const nodesToReplace = [];
        let node;
        
        while (node = walker.nextNode()) {
            const text = node.textContent;
            const lowerText = text.toLowerCase();
            const index = lowerText.indexOf(query);
            
            if (index !== -1) {
                nodesToReplace.push(node);
            }
        }
        
        nodesToReplace.forEach(node => {
            const text = node.textContent;
            const lowerText = text.toLowerCase();
            const index = lowerText.indexOf(query);
            
            if (index !== -1) {
                const before = text.substring(0, index);
                const match = text.substring(index, index + query.length);
                const after = text.substring(index + query.length);
                
                const fragment = document.createDocumentFragment();
                if (before) fragment.appendChild(document.createTextNode(before));
                
                const highlight = document.createElement('span');
                highlight.className = 'search-highlight';
                highlight.textContent = match;
                fragment.appendChild(highlight);
                
                if (after) fragment.appendChild(document.createTextNode(after));
                
                node.parentNode.replaceChild(fragment, node);
            }
        });
    }
    
    // Debounce function for performance
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Add event listener with debounce
    searchInput.addEventListener('input', debounce(function(e) {
        performSearch(e.target.value);
    }, 300));
    
    // Clear search on escape key
    searchInput.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            searchInput.value = '';
            performSearch('');
            searchInput.blur();
        }
    });
    
    // Focus search with Ctrl/Cmd + K
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            searchInput.focus();
        }
    });
});

