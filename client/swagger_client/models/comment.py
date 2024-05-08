# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST` methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token` parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Most API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible.   # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: hello@getoutline.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Comment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'data': 'object',
        'document_id': 'str',
        'parent_comment_id': 'str',
        'created_at': 'datetime',
        'created_by': 'User',
        'updated_at': 'datetime',
        'updated_by': 'User'
    }

    attribute_map = {
        'id': 'id',
        'data': 'data',
        'document_id': 'documentId',
        'parent_comment_id': 'parentCommentId',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'updated_at': 'updatedAt',
        'updated_by': 'updatedBy'
    }

    def __init__(self, id=None, data=None, document_id=None, parent_comment_id=None, created_at=None, created_by=None, updated_at=None, updated_by=None):  # noqa: E501
        """Comment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._data = None
        self._document_id = None
        self._parent_comment_id = None
        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._updated_by = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if data is not None:
            self.data = data
        if document_id is not None:
            self.document_id = document_id
        if parent_comment_id is not None:
            self.parent_comment_id = parent_comment_id
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501

        Unique identifier for the object.  # noqa: E501

        :return: The id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.

        Unique identifier for the object.  # noqa: E501

        :param id: The id of this Comment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def data(self):
        """Gets the data of this Comment.  # noqa: E501

        The editor data representing this comment.  # noqa: E501

        :return: The data of this Comment.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Comment.

        The editor data representing this comment.  # noqa: E501

        :param data: The data of this Comment.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def document_id(self):
        """Gets the document_id of this Comment.  # noqa: E501

        Identifier for the document this is related to.  # noqa: E501

        :return: The document_id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Comment.

        Identifier for the document this is related to.  # noqa: E501

        :param document_id: The document_id of this Comment.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def parent_comment_id(self):
        """Gets the parent_comment_id of this Comment.  # noqa: E501

        Identifier for the comment this is a child of, if any.  # noqa: E501

        :return: The parent_comment_id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._parent_comment_id

    @parent_comment_id.setter
    def parent_comment_id(self, parent_comment_id):
        """Sets the parent_comment_id of this Comment.

        Identifier for the comment this is a child of, if any.  # noqa: E501

        :param parent_comment_id: The parent_comment_id of this Comment.  # noqa: E501
        :type: str
        """

        self._parent_comment_id = parent_comment_id

    @property
    def created_at(self):
        """Gets the created_at of this Comment.  # noqa: E501

        The date and time that this object was created  # noqa: E501

        :return: The created_at of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Comment.

        The date and time that this object was created  # noqa: E501

        :param created_at: The created_at of this Comment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Comment.  # noqa: E501


        :return: The created_by of this Comment.  # noqa: E501
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Comment.


        :param created_by: The created_by of this Comment.  # noqa: E501
        :type: User
        """

        self._created_by = created_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Comment.  # noqa: E501

        The date and time that this object was last changed  # noqa: E501

        :return: The updated_at of this Comment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Comment.

        The date and time that this object was last changed  # noqa: E501

        :param updated_at: The updated_at of this Comment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Comment.  # noqa: E501


        :return: The updated_by of this Comment.  # noqa: E501
        :rtype: User
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Comment.


        :param updated_by: The updated_by of this Comment.  # noqa: E501
        :type: User
        """

        self._updated_by = updated_by

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Comment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Comment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other