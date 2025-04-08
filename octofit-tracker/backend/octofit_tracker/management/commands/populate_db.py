from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data by deleting objects with non-null IDs
        User.objects.filter(id__isnull=False).delete()
        Team.objects.filter(id__isnull=False).delete()
        Activity.objects.filter(id__isnull=False).delete()
        Leaderboard.objects.filter(id__isnull=False).delete()
        Workout.objects.filter(id__isnull=False).delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor Odinson'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        
        # Save users individually to ensure they are persisted in the database
        for user in users:
            user.save()

        # Create and save teams individually to ensure members are properly added
        blue_team = Team(name='Blue Team')
        blue_team.save()
        blue_team.members.set(users[:3])

        gold_team = Team(name='Gold Team')
        gold_team.save()
        gold_team.members.set(users[3:])

        # Create activities
        activities = [
            Activity(user=users[0], type='Cycling', duration=60, date=date(2025, 4, 8)),
            Activity(user=users[1], type='Crossfit', duration=120, date=date(2025, 4, 7)),
            Activity(user=users[2], type='Running', duration=90, date=date(2025, 4, 6)),
            Activity(user=users[3], type='Strength', duration=30, date=date(2025, 4, 5)),
            Activity(user=users[4], type='Swimming', duration=75, date=date(2025, 4, 4)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))