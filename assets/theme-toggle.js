const themeToggle = document.getElementById('theme-toggle');

function initializeTheme() {
    const savedTheme = getStoredTheme();
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const hour = new Date().getHours();
    const isNight = hour < 6 || hour >= 18;
    const shouldUseDark = savedTheme === 'dark' || (!savedTheme && (prefersDark || isNight));

    setTheme(shouldUseDark ? 'dark' : 'light');
}

function getStoredTheme() {
    try {
        return localStorage.getItem('theme-preference');
    } catch (e) {
        return null;
    }
}

function setStoredTheme(theme) {
    try {
        localStorage.setItem('theme-preference', theme);
    } catch (e) {
        console.warn('Could not save theme preference');
    }
}

function setTheme(theme) {
    const isDark = theme === 'dark';
    document.documentElement.classList.toggle('dark', isDark);
    themeToggle.textContent = isDark ? 'Light theme' : 'Dark theme';
    themeToggle.setAttribute('aria-label', `Switch to ${isDark ? 'light' : 'dark'} mode`);

    const lightStyle = document.querySelector('link[href="/assets/pygments-light.css"]');
    const darkStyle = document.querySelector('link[href="/assets/pygments-dark.css"]');
    
    if (lightStyle && darkStyle) {
        lightStyle.disabled = isDark;
        darkStyle.disabled = !isDark;
    }
}

function toggleTheme() {
    const currentlyDark = document.documentElement.classList.contains('dark');
    const newTheme = currentlyDark ? 'light' : 'dark';
    setTheme(newTheme);
    setStoredTheme(newTheme);
}

themeToggle.addEventListener('click', (e) => {
    e.preventDefault();
    toggleTheme();
});

initializeTheme();
