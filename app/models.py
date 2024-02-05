from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
# data = {
#         "asin": "AMZNIDNUMBER",
#         "title": "Mark 1"
# }

class Product(Model): # Table
    __keyspace__ = "scraper_app" #
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()

# surely this -> ProductScrapeEvent.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")