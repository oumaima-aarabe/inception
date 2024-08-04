// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Show/hide scroll-to-top button
    const scrollToTopButton = document.createElement('button');
    scrollToTopButton.textContent = '↑';
    scrollToTopButton.className = 'scroll-to-top';
    document.body.appendChild(scrollToTopButton);

    window.addEventListener('scroll', function() {
        if (window.scrollY > 200) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    });

    scrollToTopButton.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
