def big_files(s3, bucket, min_size):
    keys = []
    pages = s3.get_paginator("list_objects_v2").paginate(Bucket=bucket)
    for page in pages:
        for obj in page.get("Contents", []):
            if obj["Size"] >= min_size:
                keys.append(obj["Key"])
    return sorted(keys)
