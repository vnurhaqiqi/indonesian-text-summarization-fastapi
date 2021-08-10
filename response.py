from fastapi.responses import JSONResponse

STATUS_CODE = {
    200: "Success", 201: "Created", 202: "Accepted", 400: "Bad Request", 401: "Unauthorized", 403: "Forbidden",
    404: "Not Found", 405: "Method Not Acceptable", 406: "Unacceptable", 413: "Payload too large",
    429: "Too Many Requests", 500: "Internal Server Error", 501: "Not Implemented"
}


class ResponseData():
    def __init__(self):
        self.data_response = {
            'content': [],
            'status_code': None,
            'message': ""
        }

    def set_status(self, code):
        self.data_response['status_code'] = code
        self.set_message(code)

    def set_message(self, code):
        message = STATUS_CODE[code]
        self.data_response['message'] = message

    def set_content(self, data):
        self.data_response['content'] = data

    def get_response(self):
        return JSONResponse(status_code=self.data_response['status_code'], content=self.data_response)
