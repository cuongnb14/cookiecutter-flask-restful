def get_client_ip(request):
    """
    Get ip of client

    :param request:
    :return: string, ip of client
    """
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr
    return ip


def ok(data, paginator=None):
    result = {
        "status": "OK",
        "result": data,
    }
    if paginator:
        result["paginator"] = {
            "total": paginator.total,
            "offset": paginator.offset,
            "limit": paginator.limit,
        }
    return result


def fail(message, http_code):
    result = {
        "status": "Error",
        "message": message,
    }
    return result, http_code
