import os
import django
from django.core import serializers

# Set your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")  # change "Portfolio" if needed

django.setup()

# Collect all models from all installed apps
all_models = []
for app_config in django.apps.apps.get_app_configs():
    for model in app_config.get_models():
        all_models.extend(model.objects.all())

# Serialize with UTF-8
data = serializers.serialize(
    "json",
    all_models,
    use_natural_primary_keys=True,
    use_natural_foreign_keys=True,
)

with open("data.json", "w", encoding="utf-8") as f:
    f.write(data)

print("✓ Export complete — data.json created with UTF-8 encoding")
