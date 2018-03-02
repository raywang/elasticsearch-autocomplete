#create index and mapping

	curl -X PUT "http://localhost:9200/product_name/?pretty" -H 'Content-Type: application/json' --data-binary @mapping.json

# import data to es
# change index and type in util.py ,type is hardcode in mapping.json

	sudo pip install elasticsearch
	python util.py products_name.json

# check suggest api works

	curl -XPOST 'http://localhost:9200/product_name/_search?pretty' -H 'Content-Type: application/json' --data-binary  @suggest.json






