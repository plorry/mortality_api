from models import Actuary, Region

import csv
import os

def generate_actuarial_tables(filename, region_name, parent_region_name=None):
    '''
    This task takes a correctly formatted text file with Actuary data
    and generates Actuary objects for the database
    '''

    if parent_region_name:
        parent_region, created = Region.objects.get_or_create(title=parent_region_name)
    else:
        parent_region = None

    region, created = Region.objects.get_or_create(title=region_name, parent=parent_region)
    filepath = os.path.join('./data/', filename)

    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            year = row[0]
            age = row[1]
            mx = row[2]
            qx = row[3]
            ax = row[4]
            lx = row[5]
            dx = row[6]
            Lx = row[7]
            Tx = row[8]
            ex = row[9]
            actuary, act_created = Actuary.objects.get_or_create(
                year=year, age=age, region=region, defaults={
                    'mx': mx,
                    'qx': qx,
                    'ax': ax,
                    'lx': lx,
                    'dx': dx,
                    'Lx': Lx,
                    'Tx': Tx,
                    'ex': ex,
                }
            )
