# Generated by Django 3.1.7 on 2024-01-23 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eProc_Configuration', '0002_auto_20230925_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='arch_PoHeader',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('doc_number', models.CharField(db_column='DOC_NUMBER', max_length=10, verbose_name='PO Number')),
                ('version_type', models.CharField(blank=True, db_column='VERSION_TYPE', max_length=1, verbose_name='Version type')),
                ('version_num', models.CharField(blank=True, db_column='VERSION_NUM', max_length=8, verbose_name='Version number')),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=255, verbose_name='PO NAME')),
                ('total_value', models.CharField(db_column='TOTAL_VALUE', max_length=20, verbose_name='Total Value')),
                ('currency', models.CharField(db_column='CURRENCY', max_length=5, verbose_name='Currency')),
                ('requester', models.CharField(db_column='REQUESTER', max_length=12, verbose_name='Requester')),
                ('status', models.CharField(db_column='STATUS', max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(db_column='CREATED_AT', verbose_name='Created At')),
                ('created_by', models.CharField(db_column='CREATED_BY', max_length=12, verbose_name='Creator')),
                ('changed_at', models.DateTimeField(blank=True, db_column='CHANGED_AT', verbose_name='Changed At')),
                ('changed_by', models.CharField(db_column='CHANGED_BY', max_length=12, verbose_name='Changed By')),
                ('ordered_at', models.DateTimeField(blank=True, db_column='ORDERED_AT', null=True, verbose_name='Ordered At')),
                ('time_zone', models.CharField(blank=True, db_column='TIME_ZONE', max_length=6, verbose_name='Time Zone')),
                ('item_cat', models.CharField(db_column='ITEM_CAT', max_length=4, null=True, verbose_name='Item Category')),
                ('limit', models.CharField(blank=True, db_column='LIMIT', max_length=20, null=True, verbose_name='Limit')),
                ('expected_value', models.CharField(blank=True, db_column='EXPECTED_VALUE', max_length=20, null=True, verbose_name='Limit')),
                ('unlimited', models.CharField(blank=True, db_column='UNLIMITED', max_length=1, null=True, verbose_name='Unlimited')),
                ('supplier_id', models.CharField(blank=True, db_column='SUPPLIER_ID', max_length=12, null=True, verbose_name='Supplier ID')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MSS_PO_HEADER',
                'managed': True,
                'unique_together': {('client', 'doc_number')},
            },
        ),
        migrations.CreateModel(
            name='arch_ScHeader',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('doc_number', models.CharField(db_column='DOC_NUMBER', max_length=10, verbose_name='SC Number')),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=255, null=True, verbose_name='SC Name')),
                ('total_value', models.CharField(db_column='TOTAL_VALUE', max_length=15, verbose_name='Total Value')),
                ('currency', models.CharField(db_column='CURRENCY', max_length=3, verbose_name='Currency')),
                ('requester', models.CharField(db_column='REQUESTER', max_length=12, verbose_name='Requester')),
                ('status', models.CharField(db_column='STATUS', max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(db_column='CREATED_AT', verbose_name='Created At')),
                ('created_by', models.CharField(db_column='CREATED_BY', max_length=12, verbose_name='Creator')),
                ('changed_at', models.DateTimeField(blank=True, db_column='CHANGED_AT', null=True, verbose_name='Changed At')),
                ('changed_by', models.CharField(db_column='CHANGED_BY', max_length=12, verbose_name='Changed By')),
                ('ordered_at', models.DateTimeField(blank=True, db_column='ORDERED_AT', null=True, verbose_name='Ordered At')),
                ('time_zone', models.CharField(blank=True, db_column='TIME_ZONE', max_length=6, null=True, verbose_name='Time Zone')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MSS_SC_HEADER',
                'managed': True,
                'unique_together': {('client', 'doc_number')},
            },
        ),
        migrations.CreateModel(
            name='ConfHeader',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('doc_number', models.CharField(db_column='DOC_NUMBER', max_length=10, verbose_name='PO Number')),
                ('conf_sub_type', models.CharField(blank=True, db_column='CONF_SUB_TYPE', max_length=4, verbose_name='Confirmation Sub Type')),
                ('description', models.CharField(blank=True, db_column='DESCRIPTION', max_length=255, verbose_name='PO NAME')),
                ('total_value', models.CharField(db_column='TOTAL_VALUE', max_length=20, verbose_name='Total Value')),
                ('currency', models.CharField(db_column='CURRENCY', max_length=5, verbose_name='Currency')),
                ('requester', models.CharField(db_column='REQUESTER', max_length=12, verbose_name='Requester')),
                ('status', models.CharField(db_column='STATUS', max_length=20, verbose_name='Status')),
                ('created_at', models.DateTimeField(db_column='CREATED_AT', verbose_name='Created At')),
                ('created_by', models.CharField(db_column='CREATED_BY', max_length=12, verbose_name='Creator')),
                ('changed_at', models.DateTimeField(blank=True, db_column='CHANGED_AT', verbose_name='Changed At')),
                ('changed_by', models.CharField(db_column='CHANGED_BY', max_length=12, verbose_name='Changed By')),
                ('ordered_at', models.DateTimeField(blank=True, db_column='ORDERED_AT', null=True, verbose_name='Ordered At')),
                ('time_zone', models.CharField(blank=True, db_column='TIME_ZONE', max_length=6, verbose_name='Time Zone')),
                ('supplier_id', models.CharField(blank=True, db_column='SUPPLIER_ID', max_length=12, null=True, verbose_name='Supplier ID')),
                ('supplier_name', models.CharField(blank=True, db_column='SUPPLIER_Name', max_length=255, null=True, verbose_name='Supplier Name')),
                ('conf_movement', models.PositiveIntegerField(blank=True, db_column='ACC_ITEM_NUM', null=True)),
                ('po_doc_number', models.CharField(db_column='PO_DOC_NUMBER', max_length=10, verbose_name='PO Document Number')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MSS_CONF_HEADER',
                'managed': True,
                'unique_together': {('client', 'doc_number')},
            },
        ),
        migrations.CreateModel(
            name='ConfItem',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('item_num', models.CharField(blank=True, db_column='CONF_ITEM_NUM', max_length=10, null=True, verbose_name='Line Number')),
                ('po_item_num', models.CharField(blank=True, db_column='PO_ITEM_NUM', max_length=10, null=True, verbose_name='Line Number')),
                ('ref_item_guid', models.CharField(db_column='REF_ITEM_GUID', max_length=32)),
                ('prod_description', models.CharField(db_column='PROD_DESCRIPTION', max_length=255, verbose_name='Description')),
                ('comp_code', models.CharField(db_column='COMP_CODE', max_length=10, verbose_name='Company Code')),
                ('purch_grp', models.CharField(blank=True, db_column='PURCH_GRP', max_length=20, null=True, verbose_name='Purchasing Group')),
                ('purch_org', models.CharField(blank=True, db_column='PURCH_ORG', max_length=20, null=True, verbose_name='Purchasing Organization')),
                ('po_item_del_date', models.DateField(db_column='PO_ITEM_DEL_DATE', max_length=10, null=True, verbose_name='Po Item Delivery Date')),
                ('del_note_date', models.DateField(db_column='DEL_NOTE_DATE', max_length=10, null=True, verbose_name='Delivery Note Date')),
                ('prod_cat', models.CharField(db_column='PROD_CAT', max_length=20, verbose_name='Product Category')),
                ('prod_type', models.CharField(db_column='PROD_TYPE', max_length=2, verbose_name='Product Type')),
                ('catalog_id', models.CharField(blank=True, db_column='CATALOG_ID', max_length=20, null=True, verbose_name='Catalog ID')),
                ('unspsc', models.CharField(blank=True, db_column='UNSPSC', max_length=10, null=True, verbose_name='UNSPSC')),
                ('quantity', models.CharField(blank=True, db_column='QUANTITY', max_length=20, null=True, verbose_name='Quantity')),
                ('price', models.CharField(blank=True, db_column='PRICE', max_length=15, null=True, verbose_name='Price')),
                ('price_unit', models.CharField(blank=True, db_column='PRICE_UNIT', max_length=5, null=True, verbose_name='Price Unit')),
                ('unit', models.CharField(db_column='UNIT', max_length=3, verbose_name='Unit')),
                ('gross_price', models.CharField(blank=True, db_column='GROSS_PRICE', max_length=15, null=True, verbose_name='Gross Price')),
                ('supp_prod_num', models.CharField(blank=True, db_column='SUPP_PROD_NUM', max_length=40, null=True, verbose_name='Supplier Product Number')),
                ('manu_part_num', models.CharField(blank=True, db_column='MANU_PART_NUM', max_length=40, null=True, verbose_name='manu part num')),
                ('manu_code_num', models.CharField(blank=True, db_column='MANU_CODE_NUM', max_length=10, null=True, verbose_name='manu code num')),
                ('ctr_num', models.CharField(blank=True, db_column='CTR_NUM', max_length=50, null=True, verbose_name='ctr num')),
                ('goods_recep', models.CharField(db_column='GOODS_RECEP', max_length=12, verbose_name='Goods Recipient')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('header_guid', models.ForeignKey(db_column='HEADER_GUID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.confheader')),
            ],
            options={
                'db_table': 'MSS_CONF_ITEM',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConfAccounting',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('acc_item_num', models.PositiveIntegerField(blank=True, db_column='ACC_ITEM_NUM', null=True)),
                ('acc_cat', models.CharField(db_column='ACC_CAT', max_length=5, verbose_name='Account Assignment Category')),
                ('dist_perc', models.CharField(blank=True, db_column='DIST_PERC', max_length=6, null=True, verbose_name='Distribution Percentage')),
                ('gl_acc_num', models.CharField(db_column='GL_ACC_NUM', max_length=10, verbose_name='General Ledger Account')),
                ('cost_center', models.CharField(blank=True, db_column='COST_CENTER', max_length=10, null=True, verbose_name='Cost Center')),
                ('internal_order', models.CharField(blank=True, db_column='INTERNAL_ORDER', max_length=12, null=True, verbose_name='Internal Order')),
                ('generic_acc_ass', models.CharField(blank=True, db_column='GENERIC_ACC_ASS', max_length=64, null=True, verbose_name='Generic Acc Ass')),
                ('wbs_ele', models.CharField(blank=True, db_column='WBS_ELE', max_length=24, null=True, verbose_name='WBS Element')),
                ('project', models.CharField(blank=True, db_column='PROJECT', max_length=24, null=True, verbose_name='Project')),
                ('task_id', models.CharField(blank=True, db_column='TASK_ID', max_length=25, null=True, verbose_name='Task Id')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('item_guid', models.ForeignKey(blank=True, db_column='ITEM_GUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.confitem')),
            ],
            options={
                'db_table': 'MSS_CONF_ACCOUNTING',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_ScItem',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('item_num', models.PositiveIntegerField(db_column='ITEM_NUM', verbose_name='Line Number')),
                ('po_num', models.CharField(blank=True, db_column='PO_NUM', max_length=10, null=True, verbose_name='PO Number')),
                ('po_item_num', models.CharField(blank=True, db_column='PO_ITEM_NUM', max_length=10, null=True, verbose_name='Item Number')),
                ('prod_description', models.CharField(db_column='PROD_DESCRIPTION', max_length=255, verbose_name='Description')),
                ('comp_code', models.CharField(db_column='COMP_CODE', max_length=10, verbose_name='Company Code')),
                ('purch_grp', models.CharField(blank=True, db_column='PURCH_GRP', max_length=20, null=True, verbose_name='Purchasing Group')),
                ('purch_org', models.CharField(blank=True, db_column='PURCH_ORG', max_length=20, null=True, verbose_name='Purchasing Organization')),
                ('supplier_id', models.CharField(blank=True, db_column='SUPPLIER_ID', max_length=12, null=True, verbose_name='Supplier ID')),
                ('item_cat', models.CharField(blank=True, db_column='ITEM_CAT', max_length=20, null=True, verbose_name='Item Category')),
                ('prod_cat', models.CharField(db_column='PROD_CAT', max_length=20, verbose_name='Product Category')),
                ('hiring_level', models.CharField(blank=True, db_column='HIRING_LEVEL', max_length=255, null=True, verbose_name='Hiring level')),
                ('hiring_role', models.CharField(blank=True, db_column='HIRING_ROLE', max_length=255, null=True, verbose_name='Hiring role')),
                ('hiring_skill', models.CharField(blank=True, db_column='HIRING_SKILL', max_length=255, null=True, verbose_name='Hiring skill')),
                ('prod_type', models.CharField(db_column='PROD_TYPE', max_length=10, verbose_name='Product Type')),
                ('catalog_id', models.CharField(blank=True, db_column='CATALOG_ID', max_length=20, null=True, verbose_name='Catalog ID')),
                ('unspsc', models.CharField(blank=True, db_column='UNSPSC', max_length=10, null=True, verbose_name='UNSPSC')),
                ('fin_entry_ind', models.CharField(blank=True, db_column='FIN_ENTRY_IND', max_length=1, null=True, verbose_name='fin_entry_ind')),
                ('item_del_date', models.DateField(db_column='ITEM_DEL_DATE', null=True, verbose_name='Delivery Date')),
                ('quantity', models.CharField(blank=True, db_column='QUANTITY', max_length=16, null=True, verbose_name='Quantity')),
                ('price', models.CharField(db_column='PRICE', max_length=15, verbose_name='Price')),
                ('price_unit', models.CharField(blank=True, db_column='PRICE_UNIT', max_length=5, null=True, verbose_name='Price Unit')),
                ('unit', models.CharField(db_column='UNIT', max_length=3, verbose_name='Unit')),
                ('gross_price', models.CharField(db_column='GROSS_PRICE', max_length=15, verbose_name='Gross Price')),
                ('overall_limit', models.CharField(db_column='OVERALL_LIMIT', max_length=15, verbose_name='overall limit')),
                ('expected_value', models.CharField(db_column='EXPECTED_VALUE', max_length=15, verbose_name='expected value')),
                ('undef_limit', models.CharField(blank=True, db_column='UNDEF_LIMIT', max_length=1, null=True, verbose_name='undef limit')),
                ('gr_ind', models.CharField(blank=True, db_column='GR_IND', max_length=1, null=True, verbose_name='Gr ind')),
                ('dis_rej_ind', models.CharField(blank=True, db_column='DIS_REJ_IND', max_length=1, null=True, verbose_name='dis rej ind')),
                ('supp_prod_num', models.CharField(blank=True, db_column='SUPP_PROD_NUM', max_length=40, null=True, verbose_name='Supplier Product Number')),
                ('manu_part_num', models.CharField(blank=True, db_column='MANU_PART_NUM', max_length=40, null=True, verbose_name='manu part num')),
                ('manu_code_num', models.CharField(blank=True, db_column='MANU_CODE_NUM', max_length=10, null=True, verbose_name='manu code num')),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=20, null=True, verbose_name='Status')),
                ('ctr_num', models.CharField(blank=True, db_column='CTR_NUM', max_length=50, null=True, verbose_name='ctr num')),
                ('supp_ord_addr', models.CharField(blank=True, db_column='SUPP_ORD_ADDR', max_length=10, null=True, verbose_name='Supplier Ordering Address')),
                ('goods_recep', models.CharField(db_column='GOODS_RECEP', max_length=12, verbose_name='Goods Recipient')),
                ('bill_to_addr_num', models.CharField(db_column='BILL_TO_ADDR_NUM', max_length=10, verbose_name='bill to addr num')),
                ('ship_to_addr_num', models.CharField(db_column='SHIP_TO_ADDR_NUM', max_length=10, verbose_name='ship to addr num')),
                ('manu_name', models.CharField(blank=True, db_column='MANU_NAME', max_length=50, null=True, verbose_name='manu name')),
                ('supp_txt', models.CharField(blank=True, db_column='SUPP_TXT', max_length=1000, null=True, verbose_name='Supplier Text')),
                ('internal_note', models.CharField(blank=True, db_column='INTERNAL_NOTE', max_length=1000, null=True, verbose_name='Internal Note')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('header_guid', models.ForeignKey(blank=True, db_column='HEADER_GUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_scheader')),
            ],
            options={
                'db_table': 'MSS_SC_ITEM',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_ScApproval',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('step_num', models.CharField(blank=True, db_column='STEP_NUM', max_length=3, null=True, verbose_name='Sequence')),
                ('app_desc', models.CharField(blank=True, db_column='APP_DESC', max_length=60, null=True, verbose_name='Agent Determination')),
                ('proc_lvl_sts', models.CharField(blank=True, db_column='PROC_LVL_STS', max_length=10, null=True, verbose_name='Level Status')),
                ('app_sts', models.CharField(blank=True, db_column='APP_STS', max_length=20, null=True, verbose_name='Status')),
                ('app_id', models.CharField(blank=True, db_column='APP_ID', max_length=70, null=True, verbose_name='Processor')),
                ('recevied_time', models.DateTimeField(blank=True, db_column='RECEVIED_TIME', null=True, verbose_name='Received On')),
                ('proc_time', models.DateTimeField(blank=True, db_column='PROC_TIME', null=True, verbose_name='Processed On')),
                ('time_zone', models.CharField(blank=True, db_column='TIME_ZONE', max_length=6, null=True, verbose_name='Time Zone')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('header_guid', models.ForeignKey(db_column='HEADER_GUID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_scheader')),
            ],
            options={
                'db_table': 'MSS_SC_APPROVAL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_ScAccounting',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('acc_item_num', models.PositiveIntegerField(blank=True, db_column='ACC_ITEM_NUM', null=True)),
                ('acc_cat', models.CharField(db_column='ACC_CAT', max_length=5, verbose_name='Account Assignment Category')),
                ('dist_perc', models.CharField(blank=True, db_column='DIST_PERC', max_length=5, null=True, verbose_name='Distribution Percentage')),
                ('gl_acc_num', models.CharField(db_column='GL_ACC_NUM', max_length=10, verbose_name='General Ledger Account')),
                ('cost_center', models.CharField(blank=True, db_column='COST_CENTER', max_length=10, null=True, verbose_name='Cost Center')),
                ('internal_order', models.CharField(blank=True, db_column='INTERNAL_ORDER', max_length=12, null=True, verbose_name='Internal Order')),
                ('generic_acc_ass', models.CharField(blank=True, db_column='GENERIC_ACC_ASS', max_length=64, null=True, verbose_name='Generic Acc Ass')),
                ('wbs_ele', models.CharField(blank=True, db_column='WBS_ELE', max_length=24, null=True, verbose_name='WBS Element')),
                ('project', models.CharField(blank=True, db_column='PROJECT', max_length=24, null=True, verbose_name='Project')),
                ('task_id', models.CharField(blank=True, db_column='TASK_ID', max_length=25, null=True, verbose_name='Task Id')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('item_guid', models.ForeignKey(db_column='ITEM_GUID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_scitem')),
            ],
            options={
                'db_table': 'MSS_SC_ACCOUNTING',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_PoItem',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('po_item_num', models.CharField(blank=True, db_column='PO_ITEM_NUM', max_length=10, null=True, verbose_name='Line Number')),
                ('sc_num', models.CharField(blank=True, db_column='SC_NUM', max_length=10, null=True, verbose_name='SC Number')),
                ('sc_header_guid', models.CharField(blank=True, db_column='SC_HEADER_GUID', max_length=32, null=True)),
                ('item_num', models.PositiveIntegerField(blank=True, db_column='ITEM_NUM', null=True)),
                ('sc_item_guid', models.CharField(blank=True, db_column='SC_ITEM_GUID', max_length=32, null=True)),
                ('prod_description', models.CharField(db_column='PROD_DESCRIPTION', max_length=255, verbose_name='Description')),
                ('comp_code', models.CharField(db_column='COMP_CODE', max_length=10, verbose_name='Company Code')),
                ('purch_grp', models.CharField(blank=True, db_column='PURCH_GRP', max_length=20, null=True, verbose_name='Purchasing Group')),
                ('purch_org', models.CharField(blank=True, db_column='PURCH_ORG', max_length=20, null=True, verbose_name='Purchasing Organization')),
                ('item_del_date', models.DateField(db_column='ITEM_DEL_DATE', max_length=10, null=True, verbose_name='Delivery Date')),
                ('prod_cat', models.CharField(db_column='PROD_CAT', max_length=20, verbose_name='Product Category')),
                ('hiring_level', models.CharField(blank=True, db_column='HIRING_LEVEL', max_length=64, null=True)),
                ('hiring_role', models.CharField(blank=True, db_column='HIRING_ROLE', max_length=64, null=True)),
                ('hiring_skill', models.CharField(blank=True, db_column='HIRING_SKILL', max_length=64, null=True)),
                ('prod_type', models.CharField(db_column='PROD_TYPE', max_length=2, verbose_name='Product Type')),
                ('catalog_id', models.CharField(blank=True, db_column='CATALOG_ID', max_length=20, null=True, verbose_name='Catalog ID')),
                ('unspsc', models.CharField(blank=True, db_column='UNSPSC', max_length=10, null=True, verbose_name='UNSPSC')),
                ('fin_entry_ind', models.CharField(blank=True, db_column='FIN_ENTRY_IND', max_length=1, null=True, verbose_name='fin_entry_ind')),
                ('quantity', models.CharField(blank=True, db_column='QUANTITY', max_length=20, null=True, verbose_name='Quantity')),
                ('price', models.CharField(blank=True, db_column='PRICE', max_length=15, null=True, verbose_name='Price')),
                ('price_unit', models.CharField(blank=True, db_column='PRICE_UNIT', max_length=5, null=True, verbose_name='Price Unit')),
                ('unit', models.CharField(db_column='UNIT', max_length=3, verbose_name='Unit')),
                ('gross_price', models.CharField(blank=True, db_column='GROSS_PRICE', max_length=15, null=True, verbose_name='Gross Price')),
                ('gr_ind', models.CharField(blank=True, db_column='GR_IND', max_length=1, null=True, verbose_name='Gr ind')),
                ('supp_prod_num', models.CharField(blank=True, db_column='SUPP_PROD_NUM', max_length=40, null=True, verbose_name='Supplier Product Number')),
                ('manu_part_num', models.CharField(blank=True, db_column='MANU_PART_NUM', max_length=40, null=True, verbose_name='manu part num')),
                ('manu_code_num', models.CharField(blank=True, db_column='MANU_CODE_NUM', max_length=10, null=True, verbose_name='manu code num')),
                ('ctr_num', models.CharField(blank=True, db_column='CTR_NUM', max_length=50, null=True, verbose_name='ctr num')),
                ('supp_ord_addr', models.CharField(blank=True, db_column='SUPP_ORD_ADDR', max_length=10, null=True, verbose_name='Supplier Ordering Address')),
                ('del_srm_purch_doc', models.CharField(blank=True, db_column='DEL_SRM_PURCH_DOC', max_length=12, null=True, verbose_name='Deletion Indicator SRM Purchasing Document')),
                ('bill_to_addr_num', models.CharField(db_column='BILL_TO_ADDR_NUM', max_length=10, verbose_name='bill to addr num')),
                ('ship_to_addr_num', models.CharField(db_column='SHIP_TO_ADDR_NUM', max_length=10, verbose_name='ship to addr num')),
                ('goods_recep', models.CharField(db_column='GOODS_RECEP', max_length=12, verbose_name='Goods Recipient')),
                ('manu_name', models.CharField(blank=True, db_column='MANU_NAME', max_length=50, null=True, verbose_name='manu name')),
                ('del_time_days', models.CharField(blank=True, db_column='DEL_TIME_DAYS', max_length=5, null=True, verbose_name='Delivery Days')),
                ('internal_note', models.CharField(blank=True, db_column='INTERNAL_NOTE', max_length=1000, null=True, verbose_name='Internal Note')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('header_guid', models.ForeignKey(db_column='HEADER_GUID', on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_poheader')),
            ],
            options={
                'db_table': 'MSS_PO_ITEM',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_PoApproval',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('step_num', models.CharField(blank=True, db_column='STEP_NUM', max_length=3, null=True, verbose_name='Sequence')),
                ('app_desc', models.CharField(blank=True, db_column='APP_DESC', max_length=60, null=True, verbose_name='Agent Determination')),
                ('proc_lvl_sts', models.CharField(blank=True, db_column='PROC_LVL_STS', max_length=10, null=True, verbose_name='Level Status')),
                ('app_sts', models.CharField(blank=True, db_column='APP_STS', max_length=20, null=True, verbose_name='Status')),
                ('app_id', models.CharField(blank=True, db_column='APP_ID', max_length=70, null=True, verbose_name='Processor')),
                ('recevied_time', models.DateTimeField(blank=True, db_column='RECEVIED_TIME', max_length=32, null=True, verbose_name='Received On')),
                ('proc_time', models.DateTimeField(blank=True, db_column='PROC_TIME', max_length=32, null=True, verbose_name='Processed On')),
                ('time_zone', models.CharField(blank=True, db_column='TIME_ZONE', max_length=6, null=True, verbose_name='Time Zone')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('header_guid', models.ForeignKey(blank=True, db_column='HEADER_GUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_poheader')),
            ],
            options={
                'db_table': 'MSS_PO_APPROVAL',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_PoAccounting',
            fields=[
                ('guid', models.CharField(db_column='GUID', max_length=32, primary_key=True, serialize=False)),
                ('acc_item_num', models.PositiveIntegerField(blank=True, db_column='ACC_ITEM_NUM', null=True)),
                ('acc_cat', models.CharField(db_column='ACC_CAT', max_length=5, verbose_name='Account Assignment Category')),
                ('dist_perc', models.CharField(blank=True, db_column='DIST_PERC', max_length=6, null=True, verbose_name='Distribution Percentage')),
                ('gl_acc_num', models.CharField(db_column='GL_ACC_NUM', max_length=10, verbose_name='General Ledger Account')),
                ('cost_center', models.CharField(blank=True, db_column='COST_CENTER', max_length=10, null=True, verbose_name='Cost Center')),
                ('internal_order', models.CharField(blank=True, db_column='INTERNAL_ORDER', max_length=12, null=True, verbose_name='Internal Order')),
                ('generic_acc_ass', models.CharField(blank=True, db_column='GENERIC_ACC_ASS', max_length=64, null=True, verbose_name='Generic Acc Ass')),
                ('wbs_ele', models.CharField(blank=True, db_column='WBS_ELE', max_length=24, null=True, verbose_name='WBS Element')),
                ('project', models.CharField(blank=True, db_column='PROJECT', max_length=24, null=True, verbose_name='Project')),
                ('task_id', models.CharField(blank=True, db_column='TASK_ID', max_length=25, null=True, verbose_name='Task Id')),
                ('del_ind', models.BooleanField(default=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
                ('item_guid', models.ForeignKey(blank=True, db_column='ITEM_GUID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='eProc_Archiving.arch_poitem')),
            ],
            options={
                'db_table': 'MSS_PO_ACCOUNTING',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='arch_SupplierSearch',
            fields=[
                ('supplier_id', models.CharField(db_column='USERNAME', max_length=16)),
                ('first_name', models.CharField(db_column='FIRST_NAME', max_length=40, null=True)),
                ('last_name', models.CharField(db_column='LAST_NAME', max_length=40, null=True)),
                ('map_id', models.CharField(db_column='MAP_ID', max_length=8, primary_key=True, serialize=False)),
                ('client', models.ForeignKey(db_column='CLIENT', on_delete=django.db.models.deletion.PROTECT, to='eProc_Configuration.orgclients')),
            ],
            options={
                'db_table': 'MMD_SUPPLIER_SEARCH',
                'managed': True,
                'unique_together': {('client', 'supplier_id')},
            },
        ),
    ]
