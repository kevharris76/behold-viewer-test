'''xpaths'''
'''login'''
username_xpath = '.form-group:nth-child(1) .form-control' #'/html/body/div/div/div/div/div/div/div/div[2]/form/div[1]/input'
password_xpath = '.form-group+ .form-group .form-control' #'/html/body/div/div/div/div/div/div/div/div[2]/form/div[2]/input'
login_submit_xpath = '.btn-block' #'/html/body/div/div/div/div/div/div/div/div[2]/form/button'

'''create /edit lists'''
sl_create_btn = '.flex-space-between .btn-primary'
sl_edit_btn = '.flex-space-between .btn-info'
sl_delete_btn = '.flex-space-between .btn-warning'
sl_filter_textbox = '.input-group .form-control'
sl_filter_dropdown = '#studylistAssigneeFilter'
sl_table_header = '#application > div > div.DefaultLayout__studyListMenu___gmCE2.\+.DefaultLayout__rawContent___2EIaI.content > div > div > div > div:nth-child(1) > div > div.react-bs-table.react-bs-table-bordered > div.react-bs-container-header.table-header-wrapper > table'
sl_table_content = "#application > div > div.DefaultLayout__studyListMenu___gmCE2.\+.DefaultLayout__rawContent___2EIaI.content > div > div > div > div:nth-child(1) > div > div.react-bs-table.react-bs-table-bordered > div.react-bs-container-body > table"

wl_accession_tb = "AccessionNumber-filter"

login_error = "#root > div > div > div > div > div > div > div.panel-body > form > div.alert.alert-danger"
#".alert-danger"
# invalidUsername = "#root > div > div > div > div > div > div > div.panel-body > form > div.alert.alert-danger > strong"


study_view = "#selectedstudy > div"
image_view = "#selectedstudy > div > div.Pane.vertical.Pane1"
patient_details_class = "sc-bdVaJa.uFiPV"
image_details_class = "sc-bwzfXH.ektgYS"
study_details_class = "sc-htpNat.bPhEfB"
report_details_class = "sc-bxivhb.jbXvo"

'''layout buttons'''
toggle_overlay = '//*[@id="application"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[1]'
layout_1x1 = '//*[@id="application"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[2]'
layout_2x1 = '//*[@id="application"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[3]'
layout_2x2 = '//*[@id="application"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[4]'
# todo need to fix this
layout_2x1_disabled = '//*[@id="application" and @class="Toolbar__unselected___2k34g btn btn-default"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[3]'
layout_2x1_enabled = '//*[@id="application" and @class="Toolbar__selected___LGfyr btn btn-default"]/div/div[1]/div/div/div[2]/ul/div/div/div[1]/button[3]'




'''image interaction tools'''
# window level and center
wwwc_button_id = "Wwwc"
wwwc_button_disabled = '//*[@id="Wwwc" and @class="Toolbar__unselected___2k34g btn btn-default"]'
wwwc_button_enabled = '//*[@id="Wwwc" and @class="Toolbar__selected___LGfyr btn btn-default"]'
# reset image
reset_button_id = "resetImage"
reset_button_disabled = '//*[@id="resetImage" and @class="Toolbar__unselected___2k34g btn btn-default"]'
reset_button_enabled = '//*[@id="resetImage" and @class="Toolbar__selected___LGfyr btn btn-default"]'
#invert button
invert_button_id = "Invert"
invert_button_disabled = '//*[@id="Invert" and @class="Toolbar__unselected___2k34g btn btn-default"]'
invert_button_enabled = '//*[@id="Invert" and @class="Toolbar__selected___LGfyr btn btn-default"]'
#PAN
pan_button_id = "Pan"
pan_button_disabled = '//*[@id="Pan" and @class="Toolbar__unselected___2k34g btn btn-default"]'
pan_button_enabled = '//*[@id="Pan" and @class="Toolbar__selected___LGfyr btn btn-default"]'
#Zoom
zoom_button_id = "Zoom"
zoom_button_disabled = '//*[@id="Zoom" and @class="Toolbar__unselected___2k34g btn btn-default"]'
zoom_button_enabled = '//*[@id="Zoom" and @class="Toolbar__selected___LGfyr btn btn-default"]'


'''ROI tools'''
ruler_id = "Length"
ruler_enabled = '//*[@id="Length" and @class="Toolbar__selected___LGfyr btn btn-default"]'
point_id = "Probe"
point_enabled = '//*[@id="Probe" and @class="Toolbar__selected___LGfyr btn btn-default"]'
angle_id = "Angle"
angle_enabled = '//*[@id="Angle" and @class="Toolbar__selected___LGfyr btn btn-default"]'
rectangle_roi_id = "RectangleRoiText"
rectangle_roi_enabled = '//*[@id="RectangleRoiText" and @class="Toolbar__selected___LGfyr btn btn-default"]'
ellipse_roi_id = "EllipticalRoiText"
ellipse_roi_enabled = '//*[@id="EllipticalRoiText" and @class="Toolbar__selected___LGfyr btn btn-default"]'

'''disease labels'''
normalLabel = "#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(1) > div:nth-child(1) > div > div > div.text-aquamarine.col-md-4"
normalSelector = "#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(3) > div"

subOptimalLabel = "#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(2) > div:nth-child(1) > div > div > div.text-aquamarine.col-md-4"
subOptimalSelector = "#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(3) > div"

'''CXR disease list information tooltips'''
info_1 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(1) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_2 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(2) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_3 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(4) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_4 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(9) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_5 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(10) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_6 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(11) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_7 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(13) > div:nth-child(1) > div > i'
info_8 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(15) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_9 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(16) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_10 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(17) > div:nth-child(1) > div > i'
info_11 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(19) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_12 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(20) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_13 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(23) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_14 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(24) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'
info_15 = '#justified-tab-example-pane-1 > div > div > div > ul > li:nth-child(25) > div:nth-child(1) > div > div > div.col-md-offset-2.col-md-2 > i'


back_to_sl = '//*[@id="application"]/div/div[2]/div/div[2]/div/div/div[3]/div/div/button[1]'
'#application > div > div.DefaultLayout__studyDetailsMenu-2___1XXyh.\+.DefaultLayout__rawContent___2EIaI.content > div > div.col-lg-2 > div > div > div.panel-footer.Panel__fullFooter___3RBXV > div > div > button:nth-child(3)'
submit_report = '.btn-outline:nth-child(3)'
'.text-center .btn-default:nth-child(1)'