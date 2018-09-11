from django.forms import ModelForm, ValidationError
from app.models import Moment


class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'

    def clean(self):
        cleand_data = super(MomentForm, self).clean()
        content = cleand_data.get("data")
        if content is None:
            raise ValidationError("请输入Content内容")
        elif content.find("ABCD")>=0:
            raise ValidationError("不能输入敏感数字ABCD")
        return cleand_data