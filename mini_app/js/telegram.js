const tg = window.Telegram.WebApp;

tg.ready();
tg.expand();


function getRoute() {
    const params = new URLSearchParams(window.location.search);

    return params.get("route");
}


function getTelegramUserId() {
    const user = tg.initDataUnsafe?.user;

    if (!user) {
        return null;
    }

    return String(user.id);
}


function getTelegramUser() {
    return tg.initDataUnsafe?.user || null;
}