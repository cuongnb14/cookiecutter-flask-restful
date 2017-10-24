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
