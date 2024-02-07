from datetime import datetime
import random
import time
from journey.models import Journey
from django.db.models import F
from django.utils import timezone
from django.db import transaction


def create_start_nodes_for_journey(journey: Journey):
    print(f"Creating start nodes for journey {journey.id}")
    time.sleep(3 + random.random() * 2)


def start_journey_start_node_creator():
    while True:
        journeys_to_process = (
            Journey.objects.select_for_update(skip_locked=True)
            .filter()
            .order_by(F("last_processed_at").asc(nulls_first=True))[:3]
        )
        with transaction.atomic():
            if len(journeys_to_process) > 0:
                print(
                    f"Processing batch: {[journey.id for journey in journeys_to_process]}"
                )
            for journey in journeys_to_process:
                create_start_nodes_for_journey(journey)
                journey.last_processed_at = timezone.now()
                journey.save()
        time.sleep(0.05)
