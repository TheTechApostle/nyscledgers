import csv
from datetime import datetime
from .models import CorpRegister

def import_books(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            CorpRegister.objects.create(
                firstname=row['firstname'],
                lastname=row['lastname'],
                cds=row['cds'],
                pcds=row['pcds'],
                sor=row['sor'],
                statedeployed=row['statedeployed'],
                statecode=row['statecode'],
                ppa=row['ppa'],
                batch=row['batch'],
                phone=row['phone'],
                date_created=datetime.strptime(row['date_created'], '%Y-%m-%d').date(),
                status_active=row['status_active'],
                profile=row['profile']
            )

if __package__==", __package__":
    csv_file_path = '../media/documents/nysc.csv'  # Replace with your actual file path
    import_books(csv_file_path)