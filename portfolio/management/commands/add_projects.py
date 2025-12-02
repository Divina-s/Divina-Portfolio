# portfolio/management/commands/add_projects.py
from django.core.management.base import BaseCommand
from django.core.files import File
import os
from django.conf import settings
from portfolio.models import Project

class Command(BaseCommand):
    help = 'Add initial 5 projects with images to the database'

    def handle(self, *args, **kwargs):
        # Path to the folder containing the images
        image_folder = os.path.join(settings.BASE_DIR, 'media/projects/')

        projects = [
            {
                "title": "A machine learning approach to predicting migration outflows from Conflict-Affected Countries",
                "description": "Migration in conflict-affected African countries is influenced by complex economic, social, political, and environmental factors. Accurate forecasting of migration flows, including bilateral migration flows, is crucial for governments, humanitarian organizations, and communities. Timely estimates help prepare for displacement, adjust labor markets, and provide social protection. However, migration is driven by interacting factors such as conflict intensity, economic shocks, environmental disruptions, and global crises like COVID-19, making accurate prediction challenging.This project develops a forecasting framework that compares classical statistical models with modern machine learning algorithms to predict migration outflows from Cameroon, Nigeria, and Libya. The framework assesses both predictive accuracy and interpretability to provide actionable insights for policymakers.",
                "github_url": "https://github.com/Divina-s/Predicting-Migration-Flows",
                "live_url": "#",
                "image_name": "migration.jpeg"
            },
            {
                "title": "DigiChamp",
                "description": "DigiChamp is an interactive gamified web application designed to teach digital literacy to secondary school students of all academic backgrounds.",
                "github_url": "https://github.com/Divina-s/DigiChamp",
                "live_url": "https://digi-champ.vercel.app/",
                "image_name": "digichamp.png"
            },
            {
                "title": "BloomsAI",
                "description": "The objective of this project is to develop a mobile application that helps farmers diagnose crop diseases quickly and accurately. Users will be able to upload pictures of their crops, and the app will analyze the images to detect any diseases present. Additionally, the app will provide recommendations for treatment of the detected diseases. The app also features a chatbot to assist users with any crop-related queries they may have.",
                "github_url": "https://github.com/Divina-s/BloomsAI",
                "live_url": "#",
                "image_name": "blooms.jpg"
            },
            {
                "title": "Blood Donor Dashboard",
                "description": "The Blood Donation Campaign Dashboard is an interactive tool designed to aid blood donation campaigns by providing data-driven insights. This dashboard helps users analyze donor behavior, campaign success, and eligibility criteria using data visualization and machine learning. By leveraging these insights, organizations can optimize strategies and effectively target potential donors.",
                "github_url": "https://github.com/Divina-s/Blood-Donor-Dashboard",
                "live_url": "#",
                "image_name": "Blood_donor.png"
            },
            {
                "title": "Logistic Regression for Student Performance Prediction",
                "description": "A Mathematical Approach to predicting UCI student performance using logistic regression.",
                "github_url": "https://github.com/Divina-s/Logistic-Regression-for-Student-Performance-Prediction",
                "live_url": "#",
                "image_name": "logistic-regression-model-3.png"
            },
        ]

        for p in projects:
            project = Project(
                title=p["title"],
                description=p["description"],
                github_url=p.get("github_url"),
                live_url=p.get("live_url")
            )
            image_path = os.path.join(image_folder, p["image_name"])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    project.image.save(p["image_name"], File(f), save=True)
                self.stdout.write(self.style.SUCCESS(f'Added project: {p["title"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'Image not found for project: {p["title"]}'))
