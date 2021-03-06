from grano.core import db
from grano.model.common import IntBase
from grano.model.util import slugify_column


class Attribute(db.Model, IntBase):
    __tablename__ = 'attribute'

    name = db.Column(db.Unicode())
    label = db.Column(db.Unicode())
    description = db.Column(db.Unicode())
    hidden = db.Column(db.Boolean())
    schema_id = db.Column(db.Integer, db.ForeignKey('schema.id'))


    @classmethod
    def by_name(cls, schema, name):
        q = db.session.query(cls)
        q = q.filter_by(schema=schema)
        q = q.filter_by(name=name)
        return q.first()

