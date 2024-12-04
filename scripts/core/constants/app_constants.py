from scripts.config.app_configurations import DatabaseConstants


class DatabaseNames:
    ilens_configuration = DatabaseConstants.metadata_db
    ilens_assistant = DatabaseConstants.ilens_assistant_db
    project_102_diageo_db = DatabaseConstants.project_102_diageo_db


class CollectionNames:
    pass


class PSQLTableNames:
    pass


class MongoQueryConstants:
    match = "$match"
    lookup = "$lookup"
    unwind = "$unwind"
    replace_root = "$replaceRoot"
    add_fields = "$addFields"


class CommonConstants:
    date_formats = [
        "%Y-%m-%d %H:%M:%S",  # Format with time
        "%Y-%m-%dT%H:%M:%S%z",  # ISO 8601 format with timezone
        "%Y-%m-%dT%H:%M:%S.%fZ",  # ISO 8601 format with fractional seconds and 'Z'
        "%Y-%m-%d",  # Date only
    ]


class Secrets:
    LOCK_OUT_TIME_MINS = 30
    issuer = "ilens"
    alg = "HS256"
    signature_key = "kliLensKLiLensKL"


class KairosConstants:
    start_absolute = 'start_absolute'
    end_absolute = 'end_absolute'
    metrics = 'metrics'
    name = 'name'
    tags = 'tags'
    plugins = 'plugins'
    cache_time = 'cache_time'
    time_zone = 'time_zone'
    group_by = 'group_by'
    aggregators = 'aggregators'
    queries = 'queries'
    results = 'results'
