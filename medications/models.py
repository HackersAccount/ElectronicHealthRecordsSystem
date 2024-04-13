# Models for managing medication-related data based on the FHIR R4b standard.
# These models represent medications, medication requests, administrations, and other medication-related information.
# -----------------------------------------------------------------------------
# Medication: Represents a pharmaceutical product.
# MedicationRequest: Represents a request for a medication, substance, or device.
# MedicationStatement: Represents information about the administration of a medication.
# MedicationDispense: Represents the supply of a medication.
# MedicationAdministration: Represents the administration of a medication.
# MedicationUsage: Represents information about the use of a medication.
# Dosage: Represents the details of a dosage.
# Reference: A reference to another resource.
# -----------------------------------------------------------------------------

from django.db import models

# Create your models here.
from django.db import models


class Medication(models.Model):
    # Details about packaged medications
    batch = models.ForeignKey(
        'MedicationBatch',
        on_delete=models.CASCADE,
        null=True,
        related_name='medication',
        verbose_name="Details about packaged medications"
    )

    # Codes that identify this medication
    code = models.ForeignKey(
        'CodeableConcept',
        on_delete=models.SET_NULL,
        null=True,
        related_name='medication',
        verbose_name="Codes that identify this medication"
    )

    # Knowledge about this medication
    definition = models.ForeignKey(
        'MedicationKnowledge',
        on_delete=models.SET_NULL,
        null=True,
        related_name='medication',
        verbose_name="Knowledge about this medication"
    )

    # Describes the form of the item. Powder; tablets; capsule.
    doseForm = models.ForeignKey(
        'CodeableConcept',
        on_delete=models.SET_NULL,
        null=True,
        related_name='medication_dose_form',
        verbose_name="powder | tablets | capsule +"
    )

    # Organization that has authorization to market medication
    marketingAuthorizationHolder = models.ForeignKey(
        'Organization',
        on_delete=models.SET_NULL,
        null=True,
        related_name='medication',
        verbose_name="Organization that has authorization to market medication"
    )

    # A code to indicate if the medication is in active use.
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('entered-in-error', 'Entered in Error')
        ],
        null=True,
        verbose_name="active | inactive | entered-in-error"
    )

    # When the specified product code does not infer a package size, this is the specific amount of drug in the product.
    totalVolume = models.ForeignKey(
        'Quantity',
        on_delete=models.SET_NULL,
        null=True,
        related_name='medication_total_volume',
        verbose_name="When the specified product code does not infer a package size, this is the specific amount of "
                     "drug in the product"
    )


class MedicationBatch(models.Model):
    """
    Details about packaged medications.
    Information that only applies to packages (not products).
    """
    # When batch will expire
    expirationDate = models.DateTimeField(
        null=True,
        verbose_name="When batch will expire",
        help_text="When this specific batch of product will expire."
    )

    # Identifier assigned to batch
    lotNumber = models.CharField(
        max_length=255,
        null=True,
        verbose_name="Identifier assigned to batch",
        help_text="The assigned lot number of a batch of the specified product."
    )


class MedicationIngredient(models.Model):
    """
    Active or inactive ingredient.
    Identifies a particular constituent of interest in the product.
    """
    # Active ingredient indicator
    isActive = models.BooleanField(
        null=True,
        verbose_name="Active ingredient indicator",
        help_text="Indication of whether this ingredient affects the therapeutic action of the drug."
    )

    # The ingredient (substance or medication) that the ingredient.strength relates to
    item = models.ForeignKey(
        'ReferenceModel',
        on_delete=models.CASCADE,
        verbose_name="The ingredient (substance or medication) that the ingredient.strength relates to",
        help_text="The ingredient (substance or medication) that the ingredient.strength relates to. This is "
                  "represented as a concept from a code system or described in another resource (Substance or "
                  "Medication)."
    )

    # Quantity of ingredient present (CodeableConcept)
    strengthCodeableConcept = models.ForeignKey(
        'CodeableConcept',
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Quantity of ingredient present",
        help_text="Specifies how many (or how much) of the items there are in this Medication. For example, "
                  "250 mg per tablet. This is expressed as a ratio where the numerator is 250mg and the denominator "
                  "is 1 tablet but can also be expressed a quantity when the denominator is assumed to be 1 tablet."
    )

    # Quantity of ingredient present (Quantity)
    strengthQuantity = models.ForeignKey(
        'YourQuantityModel',
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Quantity of ingredient present",
        help_text="Specifies how many (or how much) of the items there are in this Medication. For example, "
                  "250 mg per tablet. This is expressed as a ratio where the numerator is 250mg and the denominator "
                  "is 1 tablet but can also be expressed a quantity when the denominator is assumed to be 1 tablet."
    )

    # Quantity of ingredient present (Ratio)
    strengthRatio = models.ForeignKey(
        'RatioModel',
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Quantity of ingredient present",
        help_text="Specifies how many (or how much) of the items there are in this Medication. For example, "
                  "250 mg per tablet. This is expressed as a ratio where the numerator is 250mg and the denominator "
                  "is 1 tablet but can also be expressed a quantity when the denominator is assumed to be 1 tablet."
    )


class CodeableConcept(models.Model):
    # Define fields for CodeableConcept model
    pass


class MedicationKnowledge(models.Model):
    # Define fields for MedicationKnowledge model
    pass


class Organization(models.Model):
    # Define fields for Organization model
    pass


class Quantity(models.Model):
    # Define fields for Quantity model
    pass
