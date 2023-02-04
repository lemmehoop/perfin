function set_timezone_cookie() {
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    document.cookie = "timezone=" + timezone;
}
