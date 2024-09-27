def get_aggregations(response, aggregation_group_name):
    try:
        aggregations = response['aggregation']['aggregations']
        data = [i for i in aggregations if i['group'] == aggregation_group_name]
        return data[0]
    except Exception as e:
        raise e


def get_aggregations_by_type(response, aggregation_group_name):
    try:
        aggregations = response['aggregation']['aggregations']
        data = [i for i in aggregations if i['type'] == aggregation_group_name]
        return data[0]
    except Exception as e:
        raise e


def get_quick_filters(response, aggregation_group_name):
    try:
        aggregations = response['aggregation']['quickFilters']
        data = [i for i in aggregations if i['group'] == aggregation_group_name]
        return data[0]
    except Exception as e:
        raise e


def get_winner_listings(elastic_contents, listing_ids):
    for i in range(len(elastic_contents)):
        listings = elastic_contents[i]['_source']['listings']
        data = [listing for listing in listings if listing['id'] == listing_ids[i]]
        return data
