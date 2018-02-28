import json
import os


class Config:

    def __init__(self):
        self.values = {}
        try:
            with open(self.config_filename(), 'r') as f:
                self.values = json.loads(f.read())
        except:
            print("Exception in Config constructor on file: " + self.config_filename())

    def config_filename(self):
        return 'config.json'

    def cosmosdb_acct(self):
        return os.environ['AZURE_COSMOSDB_GRAPH1_ACCT']

    def cosmosdb_uri(self):
        return os.environ['AZURE_COSMOSDB_GRAPH1_URI']

    def cosmosdb_gremlin_url(self):
        acct = self.cosmosdb_acct()
        return "wss://{}.gremlin.cosmosdb.azure.com:443/".format(acct)

    def cosmosdb_key(self):
        return os.environ['AZURE_COSMOSDB_GRAPH1_KEY']

    def data_dir(self):
        return os.environ['IMDB_DATA_DIR']
        # IMDB_DATA_DIR=/Users/cjoakim/Downloads/imdb

    def data_filename_raw(self, basename):
        return '{}/raw/{}'.format(self.data_dir(), basename)
        # This directory contains the raw unzipped data downloaded from IMDb
        # see http://www.imdb.com/interfaces/
        # see https://datasets.imdbws.com
        #   name.basics.tsv
        #   title.akas.tsv
        #   title.basics.tsv
        #   title.episode.tsv
        #   title.principals.tsv
        #   title.ratings.tsv

    def data_filename_processed(self, basename):
        return '{}/processed/{}'.format(self.data_dir(), basename)

    def extract_min_votes(self):
        return 58000  # Footloose -> tt0087277 6.5 58820

    def top_ratings_csv_filename(self):
        return self.data_filename_processed('top_ratings.csv')

    def movies_csv_filename(self):
        return self.data_filename_processed('movies.csv')

    def movies_json_filename(self):
        return self.data_filename_processed('movies.json')

    def principals_csv_filename(self):
        return self.data_filename_processed('principals.csv')

    def people_csv_filename(self):
        return self.data_filename_processed('people.csv')

    def people_json_filename(self):
        return self.data_filename_processed('people.json')

    def load(self):
        try:
            with open(json_filename, 'r') as json_file:
                self.values = json.loads(json_file.read())
        except:
            print("Exception in Config.load on file: " + json_filename)
            self.values = {}
