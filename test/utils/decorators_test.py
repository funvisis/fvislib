
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
                                'enable_comments',
                        'fields': (
                                'registration_required',
                                'template_name')}),)),]
    #conditional_test(dummie)
    # print dummie.fieldsets
    pp(dummie().get_form(1))

if __name__=='__main__' :
    conditional_fieldsets_test()
