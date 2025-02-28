const BASE_CLASSES =
    "fixed left-0 top-0 w-64 h-full transform transition-all duration-300 ease-in-out z-50 shadow-lg ";

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        toggleSidebar: function() {
            if (dash_clientside.callback_context.triggered_id === "open-sidebar") {
                return BASE_CLASSES + "bg-[#403f52] translate-x-0";
            }
            return BASE_CLASSES + "bg-[#403f52] -translate-x-full";
        },
    },
});
