from mongoengine import StringField, IntField, FloatField, Document, EmbeddedDocument, EmbeddedDocumentListField

class Products(Document):
    title = StringField(required=True)
    category = StringField(required=True)
    pic_url = StringField()
    price = FloatField(required=True, min_value=0.0)
    meta = {'strict': False}

    def __init__(self,title, category, price, pic_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.category = category
        self.price = price
        self.pic_url = pic_url

    @classmethod
    def from_json(cls, data ) -> 'Products':
        for dt in data:
            print(dt)

        return cls(
            title=data['title'],
            category=data['category'],
            price=float(data['price']),
            pic_url=data['pic_url']
        )
