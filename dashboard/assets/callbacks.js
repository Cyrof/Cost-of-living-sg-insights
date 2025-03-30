window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        toggleSidebar: function(mobileOpened, desktopOpened, appShellNavbar) {
            appShellNavbar["collapsed"] = {
                mobile: !mobileOpened,
                desktop: !desktopOpened,
            };
            console.log(mobileOpened);
            console.log(desktopOpened);
            console.log(appShellNavbar);
            return appShellNavbar;
        },
        setActiveNavLink: function(pathname, ...hrefs) {
            return hrefs.map((href) => href === pathname);
        },
        toggleCard: function(nClicks) {
            // Toggle based on the click count: odd -> open, even -> closed.
            if (nClicks && nClicks % 2 === 1) {
                return [true, "Show Less"];
            }

            return [false, "Read More"];
        },
    },
});
