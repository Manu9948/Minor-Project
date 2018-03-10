f1=open('data2.csv','wb')
f1.write('Patient ID number,Registry ID,Marital Status at DX,Race/Ethnicity,NHIA Derived Hispanic Origin,Sex,Age at diagnosis,Year of Birth,'+
         'Sequence Number-Central,Month of diagnosis,Year of diagnosis,Primary Site,Laterality,Histology (92-00) ICD-O-2,Behavior (92-00) ICD-O-2,'+
         'Histologic Type ICD-O-3,Behavior Code ICD-O-3,Grade,Diagnostic Confirmation,Type of Reporting Source,EOD-Tumor Size,EOD-Extension,EOD-Extension Prost Path,'+
         'EOD-Lymph Node Involv,Regional Nodes Positive,Regional Nodes Examined,EOD-Old 13 Digit,EOD-Old 2 Digit,EOD-Old 4 Digit,Coding System for EOD,'+
         'Tumor Marker 1,Tumor Marker 2,Tumor Marker 3,CS Tumor Size,CS Extension,CS Lymph Nodes,CS Mets at Dx,CS Site-Specific Factor 1,CS Site-Specific Factor 2,'+
         'CS Site-Specific Factor 3,CS Site-Specific Factor 4,CS Site-Specific Factor 5,CS Site-Specific Factor 6,CS Site-Specific Factor 25,Derived AJCC T,Derived AJCC N,'+
         'Derived AJCC M,Derived AJCC Stage Group,Derived SS1977,Derived SS2000,Derived AJCC-Flag,CS Version Input Original,CS Version Derived,CS Version Input Current,'+
         'RX Summ-Surg Prim Site,RX Summ-Scope Reg LN Sur,RX Summ-Surg Oth Reg/Dis,RX Summ-Reg LN Examined,Reason for no surgery,RX Summ-Surgery Type,RX Summ-Scope Reg 98-02,'+
         'RX Summ-Surg Oth 98-02,SEER Record Number,SEER Type of Follow-up,Age Recode <1 Year olds,Site Recode ICD-O-3/WHO 2008,Recode ICD-O-2 to 9,Recode ICD-O-2 to 10,ICCC site recode ICD-O-3/WHO 2008,'+
         'ICCC site rec extended ICD-O-3/WHO 2008,Behavior Recode for Analysis,Histology Recode-Broad Groupings,Histology Recode-Brain Groupings,CS Schema v0204+,Race recode (White Black Other),Race recode (W B AI API),'+
         'Origin recode NHIA (Hispanic Non-Hisp),SEER historic stage A,AJCC stage 3rd edition (1988-2003),SEER modified AJCC Stage 3rd ed (1988-2003),SEER Summary Stage 1977 (1995-2000),SEER Summary Stage 2000 (2001-2003),'+
         'First malignant primary indicator,State-county recode,Cause of Death to SEER site recode,COD to site rec KM,Vital Status recode,IHS Link,Summary stage 2000 (1998+),AYA site recode/WHO 2008,Lymphoma subtype recode/WHO 2008,'+
         'SEER Cause-Specific Death Classification,SEER Other Cause of Death Classification,CS Tumor Size/Ext Eval,CS Lymph Nodes Eval,CS Mets Eval,Primary by international rules,ER Status Recode Breast Cancer (1990+),PR Status Recode Breast Cancer (1990+),'+
         'CS Schema -AJCC 6th ed (previously called v1),CS Site-Specific Factor 8,CS Site-Specific Factor 10,CS Site-Specific Factor 11,CS Site-Specific Factor 13,CS Site-Specific Factor 15,CS Site-Specific Factor16,Lymph vascular invasion,Survival months,'+
         'Survival months flag,Insurance recode (2007+),Derived AJCC-7 T,Derived AJCC-7 N,Derived AJCC-7 M,Derived AJCC-7 Stage Grp,Breast Adjusted AJCC 6th T (1988+),Breast Adjusted AJCC 6th N (1988+),Breast Adjusted AJCC 6th M (1988+),Breast Adjusted AJCC 6th Stage (1988+),'+
         'CS Site-Specific Factor 7,CS Site-Specific Factor 9,CS Site-Specific Factor 12,Derived HER2 Recode (2010+),Breast Subtype (2010+),Lymphomas: Ann Arbor Staging (1983+),CS Mets at Dx-Bone,CS Mets at Dx-Brain,CS Mets at Dx-Liver,CS Mets at Dx-Lung,T value - based on AJCC 3rd (1988-2003),'+
         'N value - based on AJCC 3rd (1988-2003),M value - based on AJCC 3rd (1988-2003),Total Number of In Situ/malignant Tumors for Patient,Total Number of Benign/Borderline Tumors for Patient,Radiation Recode,Radiation to Brain or CNS Recode (1988-1997),RX Summ-Surg/Rad Seq,Chemotherapy recode (Yes No/Unk)'+'\n')


with open('RESPIR2.TXT','r') as f:
    i=0
    for line in f.readlines():
        temp=""
        temp=temp+str(line[0:8])+','
        temp=temp+str(line[8:18])+','
        temp=temp+str(line[18])+','
        temp=temp+str(line[19:21])+','
        temp=temp+str(line[22])+','
        temp=temp+str(line[23])+','
        temp=temp+str(line[24:27])+','
        temp=temp+str(line[27:31])+','
        temp=temp+str(line[34:36])+','
        temp=temp+str(line[36:38])+','
        temp=temp+str(line[38:42])+','
        temp=temp+str(line[42:46])+','
        temp=temp+str(line[46])+','
        temp=temp+str(line[47:51])+','
        temp=temp+str(line[51])+','
        temp=temp+str(line[52:56])+','
        temp=temp+str(line[56])+','
        temp=temp+str(line[57])+','
        temp=temp+str(line[58])+','
        temp=temp+str(line[59])+','
        temp=temp+str(line[60:63])+','
        temp=temp+str(line[63:65])+','
        temp=temp+str(line[65:67])+','
        temp=temp+str(line[67])+','
        temp=temp+str(line[68:70])+','
        temp=temp+str(line[70:72])+','
        temp=temp+str(line[72:85])+','
        temp=temp+str(line[85:87])+','
        temp=temp+str(line[87:91])+','
        temp=temp+str(line[91])+','
        temp=temp+str(line[92])+','
        temp=temp+str(line[93])+','
        temp=temp+str(line[94])+','
        temp=temp+str(line[95:98])+','
        temp=temp+str(line[98:101])+','
        temp=temp+str(line[101:104])+','
        temp=temp+str(line[104:106])+','
        temp=temp+str(line[106:109])+','
        temp=temp+str(line[109:112])+','
        temp=temp+str(line[112:115])+','
        temp=temp+str(line[115:118])+','
        temp=temp+str(line[118:121])+','
        temp=temp+str(line[121:124])+','
        temp=temp+str(line[124:127])+','
        temp=temp+str(line[127:129])+','
        temp=temp+str(line[129:131])+','
        temp=temp+str(line[131:133])+','
        temp=temp+str(line[133:135])+','
        temp=temp+str(line[135])+','
        temp=temp+str(line[136])+','
        temp=temp+str(line[137])+','
        temp=temp+str(line[140:146])+','
        temp=temp+str(line[146:152])+','
        temp=temp+str(line[152:158])+','
        temp=temp+str(line[158:160])+','
        temp=temp+str(line[160])+','
        temp=temp+str(line[161])+','
        temp=temp+str(line[162:164])+','
        temp=temp+str(line[165])+','
        temp=temp+str(line[169:171])+','
        temp=temp+str(line[173])+','
        temp=temp+str(line[174])+','
        temp=temp+str(line[175:177])+','
        temp=temp+str(line[190])+','
        temp=temp+str(line[191:193])+','
        temp=temp+str(line[198:203])+','
        temp=temp+str(line[203:207])+','
        temp=temp+str(line[207:211])+','
        temp=temp+str(line[217:220])+','
        temp=temp+str(line[220:223])+','
        temp=temp+str(line[223])+','
        temp=temp+str(line[225:227])+','
        temp=temp+str(line[227:229])+','
        temp=temp+str(line[229:232])+','
        temp=temp+str(line[232])+','
        temp=temp+str(line[233])+','
        temp=temp+str(line[234])+','
        temp=temp+str(line[235])+','
        temp=temp+str(line[236:238])+','
        temp=temp+str(line[238:240])+','
        temp=temp+str(line[240])+','
        temp=temp+str(line[241])+','
        temp=temp+str(line[244])+','
        temp=temp+str(line[245:250])+','
        temp=temp+str(line[254:259])+','
        temp=temp+str(line[259:264])+','
        temp=temp+str(line[264])+','
        temp=temp+str(line[265])+','
        temp=temp+str(line[266])+','
        temp=temp+str(line[267:269])+','
        temp=temp+str(line[269:271])+','
        temp=temp+str(line[271])+','
        temp=temp+str(line[272])+','
        temp=temp+str(line[273])+','
        temp=temp+str(line[274])+','
        temp=temp+str(line[275])+','
        temp=temp+str(line[276])+','
        temp=temp+str(line[277])+','
        temp=temp+str(line[278])+','
        temp=temp+str(line[279:281])+','
        temp=temp+str(line[281:284])+','
        temp=temp+str(line[284:287])+','
        temp=temp+str(line[287:290])+','
        temp=temp+str(line[290:293])+','
        temp=temp+str(line[293:296])+','
        temp=temp+str(line[296:299])+','
        temp=temp+str(line[299])+','
        temp=temp+str(line[300:304])+','
        temp=temp+str(line[304])+','
        temp=temp+str(line[310])+','
        temp=temp+str(line[311:314])+','
        temp=temp+str(line[314:317])+','
        temp=temp+str(line[317:320])+','
        temp=temp+str(line[320:323])+','
        temp=temp+str(line[323:325])+','
        temp=temp+str(line[325:327])+','
        temp=temp+str(line[327:329])+','
        temp=temp+str(line[329:331])+','
        temp=temp+str(line[331:334])+','
        temp=temp+str(line[334:337])+','
        temp=temp+str(line[337:340])+','
        temp=temp+str(line[340])+','
        temp=temp+str(line[341])+','
        temp=temp+str(line[347])+','
        temp=temp+str(line[348])+','
        temp=temp+str(line[349])+','
        temp=temp+str(line[350])+','
        temp=temp+str(line[351])+','
        temp=temp+str(line[352:354])+','
        temp=temp+str(line[354:356])+','
        temp=temp+str(line[356:358])+','
        temp=temp+str(line[358:360])+','
        temp=temp+str(line[360:362])+','
        temp=temp+str(line[362])+','
        temp=temp+str(line[363])+','
        temp=temp+str(line[364])+','
        temp=temp+str(line[365])+','
        i+=1
        f1.write(temp+'\n')
