# coding: utf-8

import os

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, "TestDatas")

htmlreport_dir = os.path.join(base_dir, "Outputs\\reports")

log_dir = os.path.join(base_dir, "Outputs\\logs\\")

screenshot_dir = os.path.join(base_dir, "Outputs\\screenshots\\")

report_dir = os.path.join(base_dir, "Outputs\\reports\\")