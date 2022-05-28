"""module changes the language of the table names in CSV Files and transfers
 along the path that is passed as an argument when calling the module"""

from click import command, option
from boto3 import client
from pandas import concat, read_csv
from sqlalchemy import create_engine


def connect_to_minio():
    """Connect to minio"""
    return client('s3',
                  endpoint_url='http://localhost:9000',
                  aws_access_key_id='root_user',
                  aws_secret_access_key='root_password',
                  region_name='us-east-1')


def connect_to_postgres():
    """Connects to postgres db"""
    return create_engine('postgresql://postgres:myPassword@localhost:5432/postgres').connect()


def get_keys(db, bucket):
    """Function returns a list of keys in minio bucket"""
    date = db.list_objects_v2(Bucket=bucket)
    return [obj['Key'] for obj in date['Contents']]


def data_redactor(data):
    """Renames italian columns to american"""
    data.rename(
        columns={
            'data': 'date',
            'stato': 'state',
            'codice_regione': 'region_code',
            'denominazione_regione': 'region_name',
            'codice_provincia': 'province_code',
            'denominazione_provincia': 'province_name',
            'sigla_provincia': 'province_abbreviation',
            'lat': 'lat',
            'long': 'long',
            'note': 'notes',
            'totale_casi': 'total_cases',
            'codice_nuts_1': 'nuts_code_1',
            'codice_nuts_2': 'nuts_code_2',
            'codice_nuts_3': 'nuts_code_3'
        },
        inplace=True
    )


def data_concatenated(minio, bucket):
    """Function returns all the data from the basket combined into one table"""
    return concat([read_csv(minio.get_object(Bucket=bucket, Key=data).get("Body"))
                   for data in get_keys(minio, bucket)], ignore_index=True)


@command()
@option('--name_bucket', default=None)
def main(name_bucket: str = None):
    """Function can take arguments from the console or called inside a script to write data via minio"""
    bucket = name_bucket
    minio = connect_to_minio()
    data = data_concatenated(minio, bucket)
    data_redactor(data)
    data.to_sql(name_bucket, con=connect_to_postgres(), if_exists='replace', index=False)


if __name__ == '__main__':
    main()
