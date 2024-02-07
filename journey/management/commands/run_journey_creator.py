from django.core.management.base import BaseCommand
from journey import services
from multiprocessing import Process

import multiprocessing as mp
import os

mp.set_start_method("fork")


class Command(BaseCommand):
    help = "Start journey start node creator"

    def handle(self, *args, **options):
        cpu_count = os.cpu_count()
        print(f"Starting {cpu_count} processes")
        processes = []
        for _ in range(cpu_count):
            p = Process(target=services.start_journey_start_node_creator)
            p.start()
            processes.append(p)

        for p in processes:
            p.join()
