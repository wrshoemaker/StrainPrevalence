from __future__ import division
import sys
import numpy
import pickle
import bz2
import gzip
import config
import math
import os.path

import diversity_utils
import figure_utils
import parse_midas_data
import prevalence_utils

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec
import plot_utils

from scipy.stats import gamma, gaussian_kde

import calculate_predicted_prevalence_mapgd

data_directory = config.data_directory
allowed_variant_types = set(['1D','4D'])

prevalence_dict_mapgd = calculate_predicted_prevalence_mapgd.load_predicted_prevalence_dict_all()
species_list = list(prevalence_dict_mapgd.keys())
species_list.sort()
n_species_row=5
nested_species_list = [species_list[x:x+n_species_row] for x in range(0, len(species_list), n_species_row)]



clade_type = 'all'
pi_type = 'pi_include_boundary'

def make_plot(variant_type, slm=True):

    if slm == True:
        slm_status = '_slm'
        slm_plot = '_slm'

    else:
        slm_status = ''
        slm_plot = '_evo'

    gs = gridspec.GridSpec(nrows=len(nested_species_list), ncols=2*n_species_row)
    fig = plt.figure(figsize = (45, 20))

    for column_idx, column in enumerate(nested_species_list):

        for row_idx, row in enumerate(column):

            ax = fig.add_subplot(gs[column_idx, row_idx])

            predicted_prevalence = prevalence_dict_mapgd[row][clade_type][pi_type][variant_type]['predicted_prevalence_mapgd%s' % slm_status]
            predicted_prevalence = numpy.asarray(predicted_prevalence)

            observed_prevalence = prevalence_dict_mapgd[row][clade_type][pi_type][variant_type]['observed_prevalence_mapgd%s' % slm_status]
            observed_prevalence = numpy.asarray(observed_prevalence)

            predicted_prevalence_no_zeros = predicted_prevalence[(observed_prevalence>0) & (predicted_prevalence>0) ]
            observed_prevalence_no_zeros = observed_prevalence[(observed_prevalence>0) & (predicted_prevalence>0) ]

            #f_max_no_zeros = f_max[(observed_prevalence>0) & (predicted_prevalence>0)]
            if len(observed_prevalence_no_zeros) == 0:
                continue

            #all_ = numpy.concatenate([predicted_prevalence_no_zeros,observed_prevalence_no_zeros])

            #re = numpy.absolute(observed_prevalence_no_zeros - predicted_prevalence_no_zeros) / observed_prevalence_no_zeros
            #re_all = numpy.absolute(observed_prevalence_all_no_zeros - predicted_prevalence_all_no_zeros) / observed_prevalence_all_no_zeros

            #xy = numpy.vstack([observed_prevalence_no_zeros, predicted_prevalence_no_zeros])
            #z = gaussian_kde(xy)(xy)
            # Sort the points by density, so that the densest points are plotted last
            #idx = z.argsort()
            #x, y, z = observed_prevalence_no_zeros[idx], predicted_prevalence_no_zeros[idx], z[idx]
            #ax.scatter(x, y, c=z, cmap=prevalence_utils.variant_cmap_dict[variant_type], s=90, alpha=0.9, edgecolor='', zorder=1)


            sorted_plot_data = prevalence_utils.plot_color_by_pt_dens(observed_prevalence_no_zeros, predicted_prevalence_no_zeros, radius=plot_utils.color_radius, loglog=1)
            x,y,z = sorted_plot_data[:, 0], sorted_plot_data[:, 1], sorted_plot_data[:, 2]

            if len(sorted_plot_data[:, 0]) > plot_utils.n_points:
                idx_ = numpy.random.choice(len(sorted_plot_data[:, 0]), size=plot_utils.n_points, replace=False)
                x = x[idx_]
                y = y[idx_]
                z = z[idx_]

            sc_ax = ax.scatter(x, y, c=numpy.sqrt(z), cmap=plot_utils.variant_cmap_dict[variant_type], s=90, alpha=0.9, edgecolors='none', zorder=1)
            
            clb_sc_ax = plt.colorbar(sc_ax, ax=ax)
            clb_sc_ax.set_label('Number of sites', size=11)


            #plt.colorbar(sc)
            
            all_ = numpy.concatenate([x, y])


            max_ = max(all_)*1.2
            min_ = min(all_)*0.8

            ax.plot([min_, max_],[min_, max_], ls='--', lw=2, c='k', zorder=2, label='1:1')
            ax.set_xlim([min_, max_])
            ax.set_ylim([min_, max_])

            ax.set_xscale('log', basex=10)
            ax.set_yscale('log', basey=10)

            ax.set_title(figure_utils.get_pretty_species_name(row), fontsize=12, fontweight='bold', color='k' )

            if (row_idx == 0) and (column_idx == 0):
                ax.legend(loc="upper left", fontsize=14)

            if (row_idx == 0):
                ax.set_ylabel('Predicted allele prevalence', fontsize=14)

            if column_idx == len(nested_species_list)-1:
                ax.set_xlabel('Observed allele prevalence', fontsize=14)

            if column_idx == len(nested_species_list)-2:
                if row_idx > len(nested_species_list[-1])-1:
                    ax.set_xlabel('Observed allele prevalence', fontsize=14)


    fig.tight_layout()
    fig.subplots_adjust(hspace=0.2)
    # dpi = 600
    fig.savefig("%spredicted_observed_prevalence_mapgd%s_%s.pdf" % (config.analysis_directory, slm_plot, variant_type), format='pdf', bbox_inches = "tight", pad_inches = 0.4, dpi=600)
    plt.close()




if __name__=='__main__':

    for allowed_variant_type in allowed_variant_types:


        #for slm_status in [True, False]:

        make_plot(variant_type=allowed_variant_type, slm=True)
