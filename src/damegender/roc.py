#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

# DESCRIPTION: This file allows to compare machine learning algorithms

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("module 'matplotlib' is not installed")
    print("try:")
    print("$ pip3 install matplotlib")
    exit()

try:
    import numpy as np
except ModuleNotFoundError:
    print("module 'numpy' is not installed")
    print("try:")
    print("$ pip3 install numpy")
    exit()

try:
    from sklearn.svm import SVC
    from sklearn.linear_model import SGDClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.naive_bayes import BernoulliNB
    from sklearn.linear_model import SGDClassifier
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import tree, metrics
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import train_test_split
    from app.dame_sexmachine import DameSexmachine    
except ModuleNotFoundError:
    print("module 'scikit-learn' is not installed")
    print("try:")
    print("$ pip3 install scikit-learn")
    exit()

from app.dame_gender import Gender
from app.dame_utils import DameUtils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ml', choices=['svc', 'sgd', 'gaussianNB', 'multinomialNB',
                                   'bernoulliNB', 'forest', 'tree', 'mlp'])
parser.add_argument('--noshow', dest='noshow', action='store_true')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()


ds = DameSexmachine()

fileallnoundefined = 'files/names/names_tests/allnoundefined.csv'
fileall = 'files/names/names_tests/all.csv'
try:
    file1 = open(fileallnoundefined, "r+")
    file2 = open(fileall, "r+")
except FileNotFoundError:
    print("The program has not found the file, it stops.")
    print("You can need execute...")
    print("$ cd files/names/names_tests/")
    print("$ ./download.sh")

X = np.array(ds.features_list(path=fileallnoundefined))
y = ds.csv2gender_list(path=fileallnoundefined)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

if (args.verbose):
    print(X)
    print(y)

if (args.ml == "svc"):
    svc = SVC(random_state=42)
    svc.fit(X_train, y_train)
    svc_disp = metrics.plot_roc_curve(svc, X_test, y_test)

elif (args.ml == "forest"):
    rfc = RandomForestClassifier(n_estimators=10, random_state=42)
    rfc.fit(X_train, y_train)
    ax = plt.gca()
    rfc_disp = metrics.plot_roc_curve(rfc, X_test, y_test, ax=ax, alpha=0.8)
    rfc_disp.plot(ax=ax, alpha=0.8)

elif (args.ml == "sgd"):
    clf = SGDClassifier(loss="log").fit(X_train, y_train)
    sgd_disp = metrics.plot_roc_curve(clf, X_test, y_test)

elif (args.ml == "gaussianNB"):
    # Create a Gaussian Classifier
    model = GaussianNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = metrics.plot_roc_curve(model, X_test, y_test)

elif (args.ml == "multinomialNB"):
    # Create a Multinomial Classifier
    model = MultinomialNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = metrics.plot_roc_curve(model, X_test, y_test)

elif (args.ml == "bernoulliNB"):
    # Create a Bernoulli Classifier
    model = BernoulliNB()
    # Train the model using the training sets
    model.fit(X_train, y_train)
    disp = metrics.plot_roc_curve(model, X_test, y_test)

elif (args.ml == "tree"):
    # Create a tree Classifier
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    disp = metrics.plot_roc_curve(clf, X_test, y_test)

elif (args.ml == "mlp"):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X_test, y_test)
    disp = metrics.plot_roc_curve(clf, X_test, y_test)

if (args.noshow):
    plt.savefig('files/images/roc_' + args.ml + '.png')
else:
    plt.savefig('files/images/roc_' + args.ml + '.png')
    plt.show()
