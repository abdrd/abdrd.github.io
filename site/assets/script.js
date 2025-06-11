const themeToggleBtn = document.getElementById('theme-toggle-btn');

function initializeTheme() {
    const savedTheme = getStoredTheme();

    if (savedTheme === 'dark' || savedTheme === 'light') {
        setTheme(savedTheme);
        return;
    }

    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const hour = new Date().getHours();
    const isNight = hour < 6 || hour >= 18;
    const shouldUseDark = prefersDark || isNight;

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
    
    themeToggleBtn.textContent = isDark ? '☀' : '☾';
    themeToggleBtn.setAttribute('aria-label', `Switch to ${isDark ? 'light' : 'dark'} mode`);

    const codeThemeLight = document.getElementById("code-theme-light");
    const codeThemeDark = document.getElementById("code-theme-dark");

    codeThemeLight.disabled = isDark;
    codeThemeDark.disabled = !(isDark);
}

function toggleTheme() {
    const currentlyDark = document.documentElement.classList.contains('dark');
    const newTheme = currentlyDark ? 'light' : 'dark';
    setTheme(newTheme);
    setStoredTheme(newTheme);
}

themeToggleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    toggleTheme();
});

initializeTheme();
