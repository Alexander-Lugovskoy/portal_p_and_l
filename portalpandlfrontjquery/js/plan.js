$(document).ready(function() {
	/*
	$('.header_menu_button').click(function() {
		$('.header_menu').toggleClass('active');
		$('.header_menu_button').toggleClass('active');
	});
	*/

	$('#plan-true-form').submit(function() {
		var inputs = $('#plan-form').children('input'); //возьмем все инпуты в форме
		var dict = {}; //словарь, куда загрузим данные из формы для отправки по api 
		// переберём массив
		$.each(inputs,function(){
		  	var id = $(this).prop('id');
		  	var value = $(this).prop('value');
		  	dict[id] = value;
		});	
		var myJSON = JSON.stringify(dict);
		$.ajax({
			  type: 'POST',
			  url: 'http://127.0.0.1:8000/setPlan/',
			  data: myJSON,
			  dataType: 'json',
			  success: function(data){ // если запрос успешен вызываем функцию
			  		$("#result").show()

			  		$("#result_proceed_input_rub .plan_field_result").text(data.proceed_input_rub);
			  		$("#result_hookah_proceeds_rub .plan_field_result").text(data.hookah_proceeds_rub);
			  		$("#result_hookah_checks_count .plan_field_result").text(data.hookah_checks_count);
			  		$("#result_hookah_checks_count_in_day .plan_field_result").text(data.hookah_checks_count_in_day);

			  		$("#result_bar_proceeds_rub .plan_field_result").text(data.bar_proceeds_rub);
			  		$("#result_bar_checks_count .plan_field_result").text(data.bar_checks_count);
			  		$("#result_bar_checks_count_in_day .plan_field_result").text(data.bar_checks_count_in_day);

			  		$("#result_kitchen_proceeds_rub .plan_field_result").text(data.kitchen_proceeds_rub);
			  		$("#result_kitchen_checks_count .plan_field_result").text(data.kitchen_checks_count);
			  		$("#result_kitchen_checks_count_id_day .plan_field_result").text(data.kitchen_checks_count_id_day);
			  		
			  		$("#result_bar_foodcost_rub .plan_field_result").text(data.bar_foodcost_rub);
			  		$("#result_bar_products_write_off_rub .plan_field_result").text(data.bar_products_write_off_rub);
			  		$("#result_bar_surplus_rub .plan_field_result").text(data.bar_surplus_percent);
			  		$("#result_bar_failure_rub .plan_field_result").text(data.bar_failure_rub);
			  		$("#result_bar_cost_price_rub .plan_field_result").text(data.bar_cost_price_rub);
			  		$("#result_bar_cost_price_percent .plan_field_result").text(data.bar_cost_price_percent);
			  		
			  		$("#result_kitchen_foodcost_rub .plan_field_result").text(data.kitchen_foodcost_rub);
			  		$("#result_kitchen_products_write_off_rub .plan_field_result").text(data.kitchen_products_write_off_rub);
			  		$("#result_kitchen_surplus_rub .plan_field_result").text(data.kitchen_surplus_rub);
			  		$("#result_kitchen_failure_rub .plan_field_result").text(data.kitchen_failure_rub);
			  		$("#result_kitchen_cost_price_rub .plan_field_result").text(data.kitchen_cost_price_rub);
			  		$("#result_kitchen_cost_price_percent .plan_field_result").text(data.kitchen_cost_price_percent);
			  		
			  		$("#result_fot_labor_zp_povar_rub .plan_field_result").text(data.fot_labor_zp_povar_rub);
			  		$("#result_fot_labor_povar_mat_help_rub .plan_field_result").text(data.fot_labor_povar_mat_help_rub);
			  		$("#result_fot_labor_povar_zp_full_rub .plan_field_result").text(data.fot_labor_povar_zp_full_rub);
			  		$("#result_fot_labor_povar_zp_full_percent .plan_field_result").text(data.fot_labor_povar_zp_full_rub);

			  		$("#result_fpr_labor_admin_zp_full .plan_field_result").text(data.fpr_labor_admin_zp_full);
			  		$("#result_total_loosers_zp .plan_field_result").text(data.total_loosers_zp);
			  		$("#result_total_administration_zp .plan_field_result").text(data.total_administration_zp);

			  		$("#result_personal_food_cost_rub .plan_field_result").text(data.personal_food_cost_rub);
			  		$("#result_rental_of_premises_percent .plan_field_result").text(data.rental_of_premises_percent);
			  		$("#result_wanish_cost_rub .plan_field_result").text(data.wanish_cost_rub);

			  		$("#result_posuda_inventar_updating_rub .plan_field_result").text(data.posuda_inventar_updating_rub);
			  		$("#result_updating_and_remont_rub .plan_field_result").text(data.posuda_inventar_updating_rub);
			  		$("#result_updating_and_remont_percent .plan_field_result").text(data.updating_and_remont_percent);
			  		$("#result_hoztovars_rub .plan_field_result").text(data.hoztovars_rub);
			  		$("#result_prochie_rashodniki_rub .plan_field_result").text(data.prochie_rashodniki_rub);
			  		$("#result_full_cost_connection .plan_field_result").text(data.full_cost_connection);

			  		$("#result_expenses_acquiring_percent_rub .plan_field_result").text(data.expenses_acquiring_percent_rub);
			  		$("#result_expenses_banking_service_rub .plan_field_result").text(data.expenses_banking_service_rub);
			  		$("#result_financial_expenses_rub .plan_field_result").text(data.financial_expenses_rub);
			  		$("#result_financial_expenses_percent .plan_field_result").text(data.financial_expenses_percent);

			  		$("#result_soc_fonds_rub .plan_field_result").text(data.soc_fonds_rub);
			  		$("#result_marketing_events_rub .plan_field_result").text(data.marketing_events_rub);
			  		$("#result_rm_p2_rub .plan_field_result").text(data.rm_p2_rub);
			  		$("#result_rm_p2_percent .plan_field_result").text(data.rm_p2_percent);
			  		$("#result_p3_sum_rub .plan_field_result").text(data.rm_p2_percent);
			  		
			  		$("#result_total_fot_and_laborcoct_rub .plan_field_result").text(data.total_fot_and_laborcoct_rub);

			  		$("#result_op1_total_rub .plan_field_result").text(data.op1_total_rub);
			  		$("#result_op1_total_percent .plan_field_result").text(data.op1_total_percent);
			  		
			  		$("#result_total_expenses_rub .plan_field_result").text(data.total_expenses_rub);
			  		$("#result_total_expenses_percent .plan_field_result").text(data.total_expenses_percent);

			  		$("#result_total_profit_rub .plan_field_result").text(data.total_profit_rub);
			  		$("#result_total_profit_percent .plan_field_result").text(data.total_profit_percent);			  		
			  		
			  			  		
			  },

		      error: function(xhr) {
            	if(xhr.status != 200) {
            		$("#ajax-error").show();
              		$("#ajax-error #ajax-error-inputs").text(myJSON);
              	}
              } 			  
		});
	});

});