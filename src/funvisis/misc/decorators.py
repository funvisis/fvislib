# -*- coding: utf-8 -*-

try:
    from collections import OrderedDict
except ImportError:
    import ordereddict as OrderectDict



def conditional_fieldsets(a_class) :
    '''
        Receive a class who could had defined 
        the conditioned_fieldsets.
        Each element inside conditioned_fieldsets
        is a tuple (Q, F), where Q is a Queryset
        and F is a fieldsets.
        If this attribute has been defined,
        it builds the actual ModelAdmin.fieldsets
        using the fieldsets included inside the
        conditioned_fieldsets attribute if the
        corresponding Queryset has passed the
        test.
        WARNING: if you define the conditioned_fieldsets
        attribute, you cannot define the fieldsets
        attribute.
    '''
    try :
        a_class.conditioned_fieldsets
    except NameError :
        return a_class
    else :
        def fieldsets_builder(cf, fixed_condition):
            fieldsets_dict = OrderedDict()
            for q, fss in cf:
                if q(fixed_condition):
                    for fs in fss:
                        if fs[0] in fieldsets_dict:
                            for key, value in fs[1].iteritems():
                                if key in fieldsets_dict[fs[0]]:
                                    fieldsets_dict[fs[0]][key] = tuple(
                                        set(
                                            fieldsets_dict[
                                                fs[0]][key])
                                        | set(value))
                                else :
                                    fieldsets_dict[fs[0]][key] = tuple(value)
                        else :
                            fieldsets_dict[fs[0]] = fs[1]
            return list(fieldsets_dict.iteritems())

        def new_get_form(self, request, obj=None, **kwargs):
            self.fieldsets = fieldsets_builder(a_class.conditioned_fieldsets, request)
            return super(a_class, self).get_form(request, obj=obj, **kwargs)

        a_class.get_form = new_get_form
        return a_class


def conditional_fieldsets_test():

    from pprint import pprint as pp

    class P(object):
        def get_form(self, request, obj=None, **kwargs):
            return self.fieldsets

    @conditional_fieldsets
    class dummie(P):
        conditioned_fieldsets = [
            (
                lambda _:True,
                (
                    (
                        None,
                        {
                            'fields': ('url', 'title', 'content', 'sites')}),
                    (
                        'Advanced options',
                        {
                            'classes': ('collapse',),
                            'fields':
                                (
                                'enable_comments',
                                'registration_required',
                                'template_name')}),)),
            (
                lambda _:False,
                (
                    (None,
                     {
                            'fields': ('url', 'title', 'content', 'sites')}),
                    (
                        'Advanced options',
                        {
                            'classes': ('collapse',),
                            'fields':
                                (
                                'enable_comments',
                                'registration_required',
                                'template_name')}),)),
            (
                lambda _:True,
                (
                    (
                        None,
                        {
                            'fields': ('urls', 'titles', 'contents', 'sites')}),
                    (
                        'Options', {
                            'classes': ('collapse',),
                            'fields': (
                                'enable_comments',
                                'registration_required',
                                'template_name')}),)),
            (
                lambda _:True,
                (
                    (
                        None, {
                        'fields': ('urls', 'titles', 'contents', 'sites')
                    }),
                    (
                        'AAOptions', {
                        'classes': ('collapse',),
                        'fields': (
                                'enable_comments',
                                'registration_required',
                                'template_name')}),)),]
    #conditional_test(dummie)
    # print dummie.fieldsets
    pp(dummie().get_form(1))

if __name__=='__main__' :
    conditional_fieldsets_test()
