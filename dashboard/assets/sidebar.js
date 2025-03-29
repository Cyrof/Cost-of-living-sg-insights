const BASE_SIDEBAR_CLASSES =
    "fixed left-0 top-0 w-64 h-full transform transition-all duration-300 ease-in-out z-50 shadow-lg ";

const BASE_LINK_CLASSES = "block px-5 py-3 text-xl font-semibold ";

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        toggleSidebar: function() {
            if (dash_clientside.callback_context.triggered_id === "open-sidebar") {
                return BASE_SIDEBAR_CLASSES + "translate-x-0";
            }
            return BASE_SIDEBAR_CLASSES + "-translate-x-full";
        },
        updateSidebarLinkColours: function(pathname, ...hrefs) {
            "block px-5 py-3  text-xl  font-semibold ";
            return hrefs.map(
                (href) =>
                    BASE_LINK_CLASSES +
                    (href === pathname
                        ? "text-[#00ff88]"
                        : "text-gray-300 hover:text-[#00ff88]"),
            );
        },
    },
});
