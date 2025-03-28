

@given(u'användaren befinner på sidan med böcker')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren befinner på sidan med böcker')


@when(u'när användaren trycker på knappen "lägg i varukorg" för "" med priserna ""')
def step_impl(context):
    raise NotImplementedError(u'STEP: When när användaren trycker på knappen "lägg i varukorg" för "" med priserna ""')


@then(u'skall varukorgen innehålla böckerna "" och ange antal "<number_of_bboks>" samt aktuell pris "0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then skall varukorgen innehålla böckerna "" och ange antal "<number_of_bboks>" samt aktuell pris "0"')


@when(u'när användaren trycker på knappen "lägg i varukorg" för "bok1" med priserna "100"')     
def step_impl(context):
    raise NotImplementedError(u'STEP: When när användaren trycker på knappen "lägg i varukorg" för "bok1" med priserna "100"')


@then(u'skall varukorgen innehålla böckerna "bok1" och ange antal "<number_of_bboks>" samt aktuell pris "100"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then skall varukorgen innehålla böckerna "bok1" och ange antal "<number_of_bboks>" samt aktuell pris "100"')


@when(u'när användaren trycker på knappen "lägg i varukorg" för "bok1, bok2" med priserna "100, 200"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When när användaren trycker på knappen "lägg i varukorg" för "bok1, bok2" med priserna "100, 200"')


@then(u'skall varukorgen innehålla böckerna "bok1, bok2" och ange antal "<number_of_bboks>" samt aktuell pris "300"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then skall varukorgen innehålla böckerna "bok1, bok2" och ange antal "<number_of_bboks>" samt aktuell pris "300"')


@when(u'när användaren trycker på knappen "lägg i varukorg" för "bok1, bok2, bok3" med priserna "100, 200, 300"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When när användaren trycker på knappen "lägg i varukorg" för "bok1, bok2, bok3" med priserna "100, 200, 300"')


@then(u'skall varukorgen innehålla böckerna "bok1, bok2, bok3" och ange antal "<number_of_bboks>" samt aktuell pris "600"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then skall varukorgen innehålla böckerna "bok1, bok2, bok3" och ange antal "<number_of_bboks>" samt aktuell pris "600"')


@given(u'användaren befinner sig på varukorg sidan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren befinner sig på varukorg sidan')


@given(u'varukorgen innehåller "bok1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given varukorgen innehåller "bok1"')


@when(u'användaren trycker på papperskorgen för "bok1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren trycker på papperskorgen för "bok1"')     


@then(u'boken skall tas bort från varukorgen och visa pris "0" samt antal "0"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then boken skall tas bort från varukorgen och visa pris "0" samt antal "0"')


@given(u'varukorgen innehåller "bok1, bok2"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given varukorgen innehåller "bok1, bok2"')


@when(u'användaren trycker på papperskorgen för "bok2"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren trycker på papperskorgen för "bok2"')     


@then(u'boken skall tas bort från varukorgen och visa pris "200" samt antal "1"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then boken skall tas bort från varukorgen och visa pris "200" samt antal "1"')


@given(u'varukorgen innehåller "bok1, bok2, bok3"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given varukorgen innehåller "bok1, bok2, bok3"')


@then(u'boken skall tas bort från varukorgen och visa pris "400" samt antal "2"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then boken skall tas bort från varukorgen och visa pris "400" samt antal "2"')


@when(u'när användaren trycker på knappen "lägg i varukorg" för boken "Ubuntu som Server" 2 gånger')
def step_impl(context):
    raise NotImplementedError(u'STEP: When när användaren trycker på knappen "lägg i varukorg" för boken "Ubuntu som Server" 2 gånger')


@then(u'antalet av boken "Ubuntu som Server" skall vara 2 i varukorgen')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then antalet av boken "Ubuntu som Server" skall vara 2 i varukorgen')


@when(u'användaren trycker på "töm varukorg"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren trycker på "töm varukorg"')


@then(u'varukorgen skall vara tom och summan skall vara noll')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then varukorgen skall vara tom och summan skall vara noll')