#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;

my $clean_Smith = `cat /dev/null > uaagents.json`;
my $check_update = `python3 ua.py > uaagents.json`;
	exit 0;
