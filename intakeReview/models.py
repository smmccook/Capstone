from django.db import models
from django.contrib.auth import get_user_model


class Request(models.Model):
    """
        ToDO - validate url against app store, add field for secondary URL if requested on both OS
    """
    user = get_user_model()

    requested_by = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    app_name = models.CharField(verbose_name='App Name:', max_length=31, unique=True)

    URL = models.URLField(verbose_name='App Store or Google Play URL from which the App can be downloaded:')
    second_URL = models.URLField(verbose_name='Second URL if this app is being requested for both Operating Systems', null=True)
    description = models.TextField(verbose_name='Purpose/Description:')
    approved_by_legal = models.BooleanField(null=True, verbose_name='Has this been approved by legal?')
    free = models.BooleanField(null=True, verbose_name='Is it free?')
    group_licensing = models.BooleanField(null=True, verbose_name='Is it available for group licensing?')
    PHI = models.BooleanField(null=True, verbose_name='Will any Protected Health Information (PHI) be stored?')
    PII = models.BooleanField(null=True, verbose_name='Will any Personally Identifiable Information (PII) be stored?')
    PCI = models.BooleanField(null=True, verbose_name='Will any Payment Card Industry Information (PCI) be stored?')
    contract_exists = models.BooleanField(null=True, verbose_name='Is there a signed contract with a third party?')
    contract = models.FileField(upload_to='requests/contracts/', verbose_name='If so please attach the contract:', null=True)
    BAA_exists = models.BooleanField(null=True, verbose_name='Is there a signed Business Associate Agreement (BAA)?')
    BAA = models.FileField(upload_to='requests/BAAs/', verbose_name='If so please attach the BAA:', null=True)
    external_access_required = models.BooleanField(null=True, verbose_name='Will there be a need for external access to'
                                                                           ' AAH systems?')
    access_forms = models.FileField(upload_to='requests/accessForms/', verbose_name='If so please attach', null=True)
    OS_version = models.CharField(verbose_name='Operating System/Version', max_length=31)
    device = models.CharField(verbose_name='Device this will be used on:', max_length=31)
    min_OS_version = models.CharField(verbose_name='Minimum OS version required for the App:', max_length=31)
    latest_release_date = models.CharField(verbose_name='Latest release date:', max_length=31)

    external_services = models.TextField(verbose_name='Does the app rely on external services or servers?'
                                                      ' (i.e Email, cloud, etc) If so, please explain')

    other_applications = models.TextField(verbose_name='Will the app need to interface with other applications or '
                                                       '              services on the device? '
                                                       '(i.e. Email, Camera, Photos, etc.) If so, please explain')

    notes = models.TextField(verbose_name='Additional Notes:', null=True)
    security_notes = models.TextField(verbose_name='Security Notes:', null=True)

    STATUS_CHOICES = [
            (0, 'Incomplete'),
            (1, 'Pending'),
            (2, 'Approved'),
            (3, 'Denied')
        ]
    status = models.IntegerField(verbose_name="Status:", choices=STATUS_CHOICES, default=0, null=True)

    time_submitted = models.DateTimeField(auto_now_add=True, blank=True)
    time_reviewed = models.DateTimeField(null=True)

    @classmethod
    def create(cls, app_name, URL, second_URL, description, approved_by_legal, free, PHI, PII, PCI, contract_exists, BAA_exists,
               external_access_required, proper_access_forms, OS_version, device, min_OS_version, latest_release_date,
               external_services, other_applications, notes, security_notes, status, time_submitted,
               time_reviewed=None, access_forms=None, BAA=None, contract=None, group_licensing=None):
        return cls(app_name=app_name, URL=URL, second_URL=second_URL, description=description, approved_by_legal=approved_by_legal, free=free,
                   PHI=PHI, PII=PII, PCI=PCI, contract_exists=contract_exists, BAA_exists=BAA_exists,
                   external_access_required=external_access_required,
                   OS_version=OS_version, device=device, min_OS_version=min_OS_version, latest_release_date=
                   latest_release_date, external_services=external_services, other_applications=other_applications,
                   security_notes=security_notes, status=status, time_submitted=time_submitted, time_reviewed=
                   time_reviewed, access_forms=access_forms, BAA=BAA, contract=contract, notes=notes,
                   group_licensing=group_licensing)

    def __str__(self):
        return self.app_name

    class Meta:
        verbose_name = 'Mobile Application Request'
        # ordering = ['time_submitted', 'app_name']
        get_latest_by = 'time_submitted'


# class User(models.Model):


class App(models.Model):
    name = models.CharField(max_length=64)
    request = models.OneToOneField
