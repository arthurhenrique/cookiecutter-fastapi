def pagenation(
    page_number=1, page_size=20, total_count=0, data=None, start_page_as_1=True
):
    """Return payload that contains metainformations about
    pagination and listing data.
    page_number starts with 0 (array like),
    if start_page_as_1 defined as True, start with 1.
    """
    if start_page_as_1:
        if page_number <= 0:
            raise Exception(
                "Page number must starts > 0.\nCause: start_page_as_1=True and page_number defined as <= 0"
            )
        else:
            page_number -= 1
    remaining = total_count % page_size
    total_pages = (
        total_count // page_size + 1 if remaining else total_count // page_size
    )
    begin = page_number * page_size
    end = begin
    if page_number == total_pages and remaining:
        end += remaining
    else:
        end += page_size
    return {
        "begin": begin,
        "end": end,
        "totalPages": total_pages,
        "remaining": remaining,
        "pageNumber": page_number,
        "pageSize": page_size,
        "totalCount": total_count,
        "listings": data[begin:end],
    }
