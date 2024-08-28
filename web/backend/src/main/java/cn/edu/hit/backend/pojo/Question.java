package cn.edu.hit.backend.pojo;

import lombok.Data;
import org.springframework.format.annotation.DateTimeFormat;

import java.time.LocalDate;

@Data
public class Question {
  private Integer id;
  private String question;
  @DateTimeFormat(pattern = "yyyy-MM-dd")
  private LocalDate create_date;
  private Integer num_agree;
  private Integer num_disagree;
  private String expert_conclusion;
}
