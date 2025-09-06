{
    "name": "AWS",
    "version": "18.0.1.0",
    "category": "Website",
    "summary": "AWS integration",
    "author": "Fedos",
    "installable": True,
    "application": True,
    "auto_install": False,
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/order_model_views.xml",
        'views/defect_reason_wizard.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "arm/static/src/css/list_view.css",
        ],
    },
    "license": "LGPL-3",
} # type: ignore
