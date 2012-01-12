# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes import generic

import choices
#import scielomanager.tools

class Collection(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(_('Collection Name'), max_length=128, db_index=True,)
    manager = models.ForeignKey(User, related_name='collection_user')
    url = models.URLField(_('Instance URL'), )
    validated = models.BooleanField(_('Validated'), default=False, )

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        ordering = ['name']

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    collection = models.ForeignKey(Collection, related_name='user_collection', blank=False)

class Institution(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(_('Institution Name'), max_length=128, db_index=True)
    acronym = models.CharField(_('Sigla'), max_length=16, db_index=True, blank=True)
    collection = models.ForeignKey(Collection, related_name='publisher_collection')
    country = models.CharField(_('Country'), max_length=32)
    state = models.CharField(_('State'), max_length=32, null=False,blank=True,)
    city = models.CharField(_('City'), max_length=32, null=False,blank=True,)
    Address = models.TextField(_('Address'), )
    Address_number = models.CharField(_('Number'), max_length=8)
    Address_complement = models.CharField(_('Complement'), max_length=128, null=False,blank=True,)
    zip_code = models.CharField(_('Zip Code'), max_length=16, null=True, blank=True)
    phone = models.CharField(_('Phone Number'), max_length=16, null=False,blank=True,)
    fax =  models.CharField(_('Fax Number'), max_length=16, null=False,blank=True,)
    cel = models.CharField(_('Cel Number'), max_length=16, null=False,blank=True,)
    mail = models.EmailField(_('Email'),)
    validated = models.BooleanField(_('Validated'), default=False,)

    def __unicode__(self):
        return u'%s' % (self.name)


class Journal(models.Model):
    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        ordering = ['title']

    @models.permalink
    def get_absolute_url(self):
        return ("/title")

    # PART 1
    creator = models.ForeignKey(User, related_name='enjoy_creator', editable=False)
    created = models.DateTimeField(_('Date of Registration'),default=datetime.now,
        editable=False)
    updated = models.DateTimeField(_('Update Date'),default=datetime.now,
        editable=False)
    collection = models.ForeignKey(Collection, related_name='journal_collection')
    institution = models.ForeignKey(Institution, related_name='journal_institution',null=False)
    title = models.CharField(_('Journal Title'),max_length=256, db_index=True)
    short_title = models.CharField(_('Short Title'),max_length=128)
    acronym = models.CharField(_('Acronym'),max_length=8)
    scielo_issn = models.CharField(_('SciELO ISSN'),max_length=8,
        choices=choices.SCIELO_ISSN,null=False,blank=True)
    print_issn = models.CharField(_('Print ISSN'),max_length=16,null=False,blank=True)
    eletronic_issn = models.CharField(_('Eletronic ISSN'),max_length=16,null=False,blank=True)
    subject_descriptors = models.CharField(_('Subject / Descriptors'),max_length=256,null=False,blank=True)
    study_area = models.CharField(_('Study Area'),max_length=256,
        choices=choices.SUBJECTS,null=False,blank=True)
    indexation_range = models.CharField(_('Indexation Range'),max_length=256,null=False,blank=True)

    #PART 2
    init_year = models.CharField(_('Initial Date'),max_length=10,null=True,blank=True)
    init_vol = models.CharField(_('Initial Volume'), max_length=4,null=False,blank=True)
    init_num = models.CharField(_('Initial Number'), max_length=4,null=False,blank=True)
    final_year = models.CharField(_('Final Date'),max_length=10,null=True,blank=True)
    final_vol = models.CharField(_('Final Volume'),max_length=4,null=False,blank=True)
    final_num = models.CharField(_('Final Number'),max_length=4,null=False,blank=True)
    frequency = models.CharField(_('Frequency'),max_length=16,
        choices=choices.FREQUENCY,null=False,blank=True)
    pub_status = models.CharField(_('Publication Status'),max_length=16,
        choices=choices.PUBLICATION_STATUS,null=False,blank=True)
    alphabet =  models.CharField(_('Alphabet'),max_length=16,
        choices=choices.ALPHABET,null=False,blank=True)
    classification = models.CharField(_('Classification'), max_length=16,null=False,blank=True)
    national_code = models.CharField(_('National Code'), max_length=16,null=False,blank=True)
    text_language = models.CharField(_('Text Language'), max_length=259,null=False,blank=True)
    abst_language = models.CharField(_('Abstract Language'), max_length=256,null=False,blank=True)
    editorial_standard = models.CharField(_('Editorial Standard'),max_length=64,
        choices=choices.STANDARD,null=False,blank=True)
    ctrl_vocabulary = models.CharField(_('Controlled Vocabulary'),max_length=64,
        choices=choices.CTRL_VOCABULARY,null=False,blank=True)
    literature_type = models.CharField(_('Literature Type'),max_length=64,
        choices=choices.LITERATURE_TYPE,null=False,blank=True)
    treatment_level = models.CharField(_('Treatment Type'),max_length=64,
        choices=choices.TREATMENT_LEVEL,null=False,blank=True)
    pub_level = models.CharField(_('Publication Level'),max_length=64,
        choices=choices.PUBLICATION_LEVEL,null=False,blank=True)
    secs_code = models.CharField(_('SECS Code'), max_length=64,null=False,blank=True)
    validated = models.BooleanField(_('Validated'), default=False,null=False,blank=True )

class JournalMission(models.Model):
    journal = models.ForeignKey(Journal,null=False)
    description = models.TextField(_('Mission'),null=False)
    language = models.CharField(_('Language'),null=False, max_length=2)

class JournalTitleOtherForms(models.Model):
    journal = models.ForeignKey(Journal,null=False)
    form = models.CharField(_('Title'),null=False,max_length=128)
    form_sub = models.CharField(_('Sub Title'),null=False,max_length=128)
    title_type = models.CharField(_('Title Type'),max_length=16,
        choices=choices.TITLE_TYPE,null=True,)

class JournalShortTitleOtherForms(models.Model):
    title = models.ForeignKey(Journal,null=False)
    form = models.CharField(_('Short Title'),null=False,max_length=128)
    title_type = models.CharField(_('Short Title Type'),max_length=16,
        choices=choices.TITLE_TYPE,null=True,)

class UseLicense(models.Model):
    license_code = models.CharField(_('License Code'), null=False, blank=False, max_length=64)
    reference_url = models.URLField(_('License Reference URL'), null=False, blank=False)
    disclaimer = models.TextField(_('Disclaimer'), null=False, blank=False, max_length=512)

    def __unicode__(self):
        return self.license_code

class Section(models.Model):
    title = models.CharField(_('Title'), null=True, blank=True, max_length=256) #l10n
    code = models.CharField(_('Code'), null=True, blank=True, max_length=16)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Issue(models.Model):
    section = models.ManyToManyField(Section)
    journal = models.ForeignKey(Journal, null=True, blank=False)
    title = models.CharField(_('Issue Title'), null=True, blank=True, max_length=256)
    volume = models.CharField(_('Volume'), null=True, blank=True, max_length=16)
    number = models.CharField(_('Number'), null=True, blank=True, max_length=16)
    is_press_release = models.BooleanField(_('Is Press Release?'), default=False, null=False, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publication_date = models.DateField(null=False, blank=False)
    is_available = models.BooleanField(_('Is Available?'), default=False, null=False, blank=True) #status v42
    is_marked_up = models.BooleanField(_('Is Marked Up?'), default=False, null=False, blank=True) #v200
    bibliographic_strip = models.CharField(_('Custom Bibliographic Strip'), null=True, blank=True, max_length=128) #l10n
    use_license = models.ForeignKey(UseLicense, null=False)
    publisher_fullname = models.CharField(_('Publisher Full Name'), null=True, blank=True, max_length=128)
    total_documents = models.IntegerField(_('Total of Documents'), null=False, blank=False, default=0)
    ctrl_vocabulary = models.CharField(_('Controlled Vocabulary'), max_length=64,
        choices=choices.CTRL_VOCABULARY, null=False, blank=True)
    editorial_standard = models.CharField(_('Editorial Standard'), max_length=64,
        choices=choices.STANDARD, null=False, blank=True)

    def __unicode__(self):
        return self.title

class Supplement(Issue):
    suppl_label = models.CharField(_('Supplement Label'), null=True, blank=True, max_length=256)