# Generated by Django 4.2.13 on 2024-09-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_tomato_rice_cucumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cucumber',
            old_name='Anthracnose',
            new_name='anthracnose',
        ),
        migrations.RenameField(
            model_name='cucumber',
            old_name='BacterialWilt',
            new_name='bacterial_wilt',
        ),
        migrations.RenameField(
            model_name='cucumber',
            old_name='DownyMildew',
            new_name='downy_wildew',
        ),
        migrations.RenameField(
            model_name='cucumber',
            old_name='GummyStemBlight',
            new_name='gummy_stem_blight',
        ),
        migrations.RenameField(
            model_name='cucumber',
            old_name='Healthy',
            new_name='healthy',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='BacterialLeafBlight',
            new_name='bacterial_leaf_blight',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='BrownSpot',
            new_name='brown_spot',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='Healthy',
            new_name='healthy',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='LeafBlast',
            new_name='leaf_blast',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='LeafScald',
            new_name='leaf_scald',
        ),
        migrations.RenameField(
            model_name='rice',
            old_name='SheathBlight',
            new_name='sheath_blight',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='BacterialSpot',
            new_name='bacterial_spot',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='EarlyBlight',
            new_name='early_blight',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='Healthy',
            new_name='healthy',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='LateBlight',
            new_name='late_blight',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='LeafMold',
            new_name='leaf_mold',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='SeptoriaLeafSpot',
            new_name='septoria_leaf_spot',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='SpiderMites',
            new_name='spider_mites',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='TargetSpot',
            new_name='target_spot',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='TomatoMosaicVirus',
            new_name='tomato_mosaic_virus',
        ),
        migrations.RenameField(
            model_name='tomato',
            old_name='YellowLeafCurlVirus',
            new_name='yellow_leaf_curl_virus',
        ),
    ]
