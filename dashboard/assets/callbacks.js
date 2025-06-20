window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        updateSidebarState: function(mobileOpened, desktopOpened, pathname, overlayClicks, appShellNavbar){
            var ctx = dash_clientside.callback_context;
            var trigger = ctx.triggered[0].prop_id;
            var resetBurgers = false

            // url change or overlay clicked, close sidebar
            if(trigger.includes("url.pathname") || trigger.includes("sidebar-overlay.n_clicks")){
                appShellNavbar["collapsed"] = { mobile: true, desktop: true };
                resetBurgers = true;
                return [
                    appShellNavbar, 
                    { "display": "none" },
                    resetBurgers ? false : mobileOpened,
                    resetBurgers ? false : desktopOpened
                ];
            } else {
                // toggle based on burger state
                var collapsed = { mobile: !mobileOpened, desktop: !desktopOpened };
                appShellNavbar["collapsed"] = collapsed;

                // show overlay is sidebar open
                var isOpen = (!collapsed.mobile || !collapsed.desktop);
                var overlayStyle = isOpen ? {
                    "display": "block",
                } : {
                    "display": "none"
                };
                return [
                    appShellNavbar, 
                    overlayStyle,
                    mobileOpened,
                    desktopOpened
                ];
            }
        },
        setActiveNavLink: function(pathname, ...hrefs) {
            return hrefs.map((href) => href === pathname);
        },
        toggleCard: function(nClicks) {
            if (nClicks && nClicks % 2 === 1) {
                return [true, "Show Less"];
            }
            return [false, "Read More"];
        }
    }
})